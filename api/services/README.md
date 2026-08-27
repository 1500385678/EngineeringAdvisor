# `api/services/` — 业务服务层

> 按业务域切分,每个子模块负责一个领域的核心逻辑。

## 职责

- 业务编排:接 routers 进来的参数,调 lib/core 完成实际工作
- 跨子域协调:advisory 可能要 adr 库 + 团队历史 + LLM 协同
- 不感知 HTTP:没有 `Request`/`Response`,只有纯函数 + Pydantic model

## 上下游关系

```
routers  ──HTTP 协议层──▶  services  ──业务编排──▶  core / lib / models
                            │
                            └─ 调外部:LLM / DB / 飞书 / Neo4j
```

## 不做什么

- ❌ 不解析 HTTP 参数(`Request.body()` 等)
- ❌ 不返回状态码(`raise HTTPException` 也不行,改为 raise 业务异常)
- ❌ 不直接 import routers(反向依赖)

## 扩展点(按 Phase 推进)

| 子模块 | 业务 | Phase |
|---|---|---|
| `feishu_bot.py` | 飞书 bot 消息处理 + webhook 验签 | Phase 0 |
| `advisory.py` | 选型推荐(LLM + RAG 团队历史) | Phase 1 |
| `adr.py` | ADR CRUD + 版本 + 状态机 | Phase 1 |
| `radar.py` | 技术雷达聚合(依赖扫描) | Phase 1 |
| `code_review.py` | PR 自动审查(LLM + 内部规范) | Phase 2 |
| `reliability.py` | 依赖图 + 事故复盘 | Phase 3 |

## 当前状态

- `__init__.py` 已建,空包
- 第一个落地预计是 `feishu_bot.py`(Phase 0 启动时)
