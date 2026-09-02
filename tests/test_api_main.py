"""`api/main.py` 三个元端点的契约测试。

- 验证 0827 FastAPI 骨架(commit `dd0c15e`)的端点契约
- 用 `fastapi.testclient.TestClient`(基于 httpx 同步)直接调用 `create_app()` 工厂
- 不依赖真实 uvicorn 启动,`pip install -e .` 后 `pytest tests/test_api_main.py -v` 即可

后续 Phase 0 验收时,这些用例作为"骨架未回退"的最低回归保护。
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from api.main import create_app


def test_root_returns_project_identity() -> None:
    """`GET /` 返回项目代号 / Agent / 行业 / 版本 / 阶段。"""
    client = TestClient(create_app())
    response = client.get("/")
    assert response.status_code == 200

    body = response.json()
    assert body["project"] == "engineering-advisor"
    assert body["agent"] == "29-工程"
    assert body["industry"] == "工程-Engineering Level"
    assert body["version"] == "0.1.0"
    assert body["stage"] == "phase-0-scaffold"
    assert body["docs"] == "/docs"


def test_healthz_returns_ok() -> None:
    """`GET /healthz` 固定 `status=ok` + env + 启动时间,供 K8s 探活。"""
    client = TestClient(create_app())
    response = client.get("/healthz")
    assert response.status_code == 200

    body = response.json()
    assert body["status"] == "ok"
    assert body["env"] in {"development", "staging", "production", "test"}
    assert body["version"] == "0.1.0"
    assert "started_at" in body and body["started_at"].endswith("+00:00")


def test_info_endpoint_returns_uptime() -> None:
    """`GET /api/v1/info` 详情 + uptime 非负数。"""
    client = TestClient(create_app())
    response = client.get("/api/v1/info")
    assert response.status_code == 200

    body = response.json()
    assert body["agent"] == "29-工程-Engineering Level"
    assert body["industry"] == "工程-Engineering Level"
    assert body["env"] in {"development", "staging", "production", "test"}
    assert isinstance(body["debug"], bool)
    assert body["uptime_seconds"] >= 0.0
