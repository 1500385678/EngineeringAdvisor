"""HTTP 路由层(API endpoints)。

按 URL 前缀切分,每个子模块注册一组相关路由。
- 与 `services/` 关系:routers 是"薄壳",所有非 HTTP 逻辑下沉到 services
- 与 `main.py` 关系:本层不在 `create_app()` 内联,后续用 `app.include_router()` 注入

预留路由(按 Phase 推进):
- `meta.py`        `/`、`/healthz`、`/api/v1/info`(本骨架已内联在 main.py,0829 决定是否拆出)
- `advisory.py`    `/api/v1/advisory` 选型推荐(Phase 1)
- `adrs.py`        `/api/v1/adrs`     ADR 库 CRUD(Phase 1)
- `radar.py`       `/api/v1/radar`    技术雷达(Phase 1)
- `code_review.py` `/api/v1/reviews`  PR 审查回调(Phase 2)
- `webhooks/`      飞书事件订阅(Phase 0 bot 雏形)
"""

__all__: list[str] = []
