"""业务服务层(business services)。

按"业务域"切分,每个子模块负责一个领域的核心逻辑。
- 与 `routers/` 关系:routers 只做 HTTP 协议层(参数解析/响应序列化/状态码),业务逻辑全部下沉到 services
- 与 `core/` 关系:core 是"基础设施配置"(settings/db 连接池),services 是"业务编排"
- 与 `models/` 关系:models 是 DTO/ORM 数据结构,services 消费/产出这些数据结构

预留子模块(按 Phase 0/1/2 推进):
- `feishu_bot.py`    飞书 bot 消息处理(Phase 0)
- `advisory.py`      选型推荐(Phase 1 MVP)
- `adr.py`           ADR CRUD + 版本(Phase 1 MVP)
- `code_review.py`   PR 自动审查(Phase 2)
- `reliability.py`   依赖图 + 事故复盘(Phase 3)
- `radar.py`         技术雷达聚合(Phase 1)
"""

__all__: list[str] = []
