"""FastAPI app 入口。

最小可入库骨架(2026-08-27 T4 日增量):
- `GET /`         项目标识 + 版本 + 当前阶段
- `GET /healthz`  健康检查(供后续 K8s/进程守护探活)
- `GET /api/v1/info`  详情(行业/Agent/启动时间)

启动方式(pip install -e . 后):
    uvicorn api.main:app --reload --port 8000
    # 或 python -m api.main
"""

from __future__ import annotations

import time
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from api import __version__
from api.core.config import settings
from api.models.schemas import HealthResponse, InfoResponse, RootResponse

# 启动时间(进程级单例,UTC ISO 格式)
_STARTED_AT = datetime.now(timezone.utc).isoformat()


def create_app() -> FastAPI:
    """工厂函数:便于测试覆盖与多实例。"""
    app = FastAPI(
        title="EngineeringAdvisor API",
        description="29-工程 行业顾问产品后端 - 工程基础脚手架 v0.1",
        version=__version__,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    @app.get("/", response_model=RootResponse, tags=["meta"])
    async def root() -> RootResponse:
        """根路由:项目标识 + 当前阶段。"""
        return RootResponse(
            project="engineering-advisor",
            agent="29-工程",
            industry="工程-Engineering Level",
            version=__version__,
            stage="phase-0-scaffold",
            docs="/docs",
        )

    @app.get("/healthz", response_model=HealthResponse, tags=["meta"])
    async def healthz() -> HealthResponse:
        """健康检查:K8s liveness/readiness 探活。"""
        return HealthResponse(
            status="ok",
            env=settings.env,
            version=__version__,
            started_at=_STARTED_AT,
        )

    @app.get("/api/v1/info", response_model=InfoResponse, tags=["meta"])
    async def info() -> InfoResponse:
        """详情:行业 / Agent / 启动时间 / 配置来源。"""
        return InfoResponse(
            agent="29-工程-Engineering Level",
            industry="工程-Engineering Level",
            version=__version__,
            env=settings.env,
            debug=settings.debug,
            started_at=_STARTED_AT,
            uptime_seconds=round(time.time() - _parse_started(_STARTED_AT), 3),
        )

    return app


def _parse_started(iso: str) -> float:
    """从 ISO 时间反推 epoch 秒(供 uptime 计算)。"""
    return datetime.fromisoformat(iso).timestamp()


# uvicorn 入口:`uvicorn api.main:app`
app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
