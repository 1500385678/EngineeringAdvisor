"""通用工具层(cross-cutting utilities)。

不依赖任何业务域,只放"全栈都会用到"的基础组件。
当前为空包,后续按需增量:
- `logging.py`     结构化日志(JSON + trace_id)
- `exception.py`   业务异常类 + 全局异常处理器
- `retry.py`       指数退避重试(供外部 API/DB 调用)
- `http_client.py` httpx 共享客户端(Phase 0 飞书 bot 入口)
- `time.py`        UTC/本地时区互转(避免 datetime 滥用)

**注意**:本层禁止 `import api.services` 或 `api.routers`(避免循环依赖)。
"""

__all__: list[str] = []
