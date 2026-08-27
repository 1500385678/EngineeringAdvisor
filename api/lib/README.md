# `api/lib/` — 通用工具层

> 跨业务域可复用的基础组件。不依赖任何具体业务逻辑。

## 职责

放"全栈都会用到"的小工具,业务侧随手 `from api.lib.logging import get_logger` 即可。

## 不做什么

- ❌ 不引入业务域(禁止 `import api.services`)
- ❌ 不做 HTTP 路由(那是 `routers/`)
- ❌ 不持有数据库连接/全局单例(那是 `core/`)

## 扩展点(后续按需增量)

| 子模块 | 用途 | 触发时机 |
|---|---|---|
| `logging.py` | 结构化日志(JSON + trace_id) | Phase 0 调试飞书 bot |
| `exception.py` | 业务异常类 + 全局处理器 | Phase 1 ADR 检索开始有错误处理 |
| `retry.py` | 指数退避重试 | 外部 API/DB 调用 > 3 次 |
| `http_client.py` | httpx 共享 client | Phase 0 飞书 webhook |
| `time.py` | UTC/本地时区 | 事故复盘时间线 |

## 当前状态

- `__init__.py` 已建(0 业务代码),空包
- 与 `api/core/` 的边界:core 是"配置中心",lib 是"工具箱"
