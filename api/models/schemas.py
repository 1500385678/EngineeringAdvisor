"""基础 DTO(请求/响应模型)。

本阶段只覆盖 `/` `/healthz` `/api/v1/info` 三个端点的响应。
后续 Phase 1+ 在此追加 `AdvisoryRequest` / `IssueBrief` 等业务 DTO。
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class RootResponse(BaseModel):
    """`GET /` 响应:项目标识 + 当前阶段。"""

    project: str = Field(..., description="项目代号,小写连字符")
    agent: str = Field(..., description="Agent 名,如 29-工程")
    industry: str = Field(..., description="行业分类全称")
    version: str = Field(..., description="当前版本号(语义化版本)")
    stage: str = Field(..., description="当前阶段,如 phase-0-scaffold")
    docs: str = Field(..., description="OpenAPI 文档路径")


class HealthResponse(BaseModel):
    """`GET /healthz` 响应:探活用。"""

    status: str = Field(..., description="健康状态,固定 'ok'")
    env: str = Field(..., description="运行环境")
    version: str = Field(..., description="服务版本")
    started_at: str = Field(..., description="进程启动时间(UTC ISO)")


class InfoResponse(BaseModel):
    """`GET /api/v1/info` 响应:详情。"""

    agent: str = Field(..., description="Agent 标识")
    industry: str = Field(..., description="行业分类")
    version: str = Field(..., description="服务版本")
    env: str = Field(..., description="运行环境")
    debug: bool = Field(..., description="debug 模式")
    started_at: str = Field(..., description="进程启动时间(UTC ISO)")
    uptime_seconds: float = Field(..., description="运行时长(秒)")
