# `api/routers/` — HTTP 路由层

> 薄壳:只做 HTTP 协议层,业务逻辑下沉到 `services/`。

## 职责

- 解析参数(query/path/body)+ 校验 Pydantic schema
- 调对应 service
- 序列化响应 + 设置状态码
- 注册路由到 `app`:`app.include_router(advisory_router, prefix="/api/v1")`

## 不做什么

- ❌ 不写业务逻辑(超过 5 行的判断/循环/计算,挪到 services)
- ❌ 不直接调 LLM/DB/外部 API(那是 services 的活)
- ❌ 不定义全局中间件/异常处理(那是 `main.py` 的活)

## 路由切分

| 子模块 | URL 前缀 | Phase |
|---|---|---|
| `meta.py` | `/`、`/healthz`、`/api/v1/info` | Phase 0(0829 决定是否从 main.py 拆出) |
| `advisory.py` | `/api/v1/advisory` | Phase 1 |
| `adrs.py` | `/api/v1/adrs` | Phase 1 |
| `radar.py` | `/api/v1/radar` | Phase 1 |
| `code_review.py` | `/api/v1/reviews` | Phase 2 |
| `webhooks/feishu.py` | `/webhooks/feishu` | Phase 0 |

## 当前状态

- `__init__.py` 已建,空包
- 现有 3 个端点内联在 `api/main.py` 的 `create_app()` 内,**0829 README 升级时一并评估是否拆出**
