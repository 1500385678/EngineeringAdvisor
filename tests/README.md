# `tests/` — pytest 测试根

> 镜像 `api/` 结构,1:1 对应。

## 约定

- 文件名 `test_*.py` 或 `*_test.py`,pytest 自动发现
- 根目录有 `conftest.py`(后续加),提供共享 fixture(`app`/`client`/`db`)
- 单元测试不需要 DB 时,用 `monkeypatch` 替换 settings
- 集成测试需要 DB 时,推荐 `pytest-postgresql` 或 testcontainers

## 目录布局(预期)

```
tests/
├── __init__.py
├── conftest.py                  # 共享 fixture
├── test_api_main.py             # 三个端点
├── test_core_config.py          # 配置加载
├── test_services_advisory.py    # Phase 1
├── test_routers_adrs.py         # Phase 1
└── test_lib_logging.py          # 结构化日志
```

## 运行

```bash
# 全部
pytest -v

# 单文件
pytest tests/test_api_main.py -v

# 覆盖率
pytest --cov=api --cov-report=term-missing
```

## 当前状态

- `__init__.py` 已建,无 conftest.py、无测试用例
- **首个测试用例建议是 `test_api_main.py`**:验证 `/` `/healthz` `/api/v1/info` 三个端点返回 200 + 字段,作为 0827 FastAPI 骨架的回归保护
