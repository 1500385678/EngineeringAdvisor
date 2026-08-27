"""pytest 测试根包。

镜像 `api/` 目录结构,子包命名 1:1 对应:
- `tests/test_api_main.py`        验证 main.py 三个端点
- `tests/test_core_config.py`     配置加载(覆盖 .env / 环境变量)
- `tests/test_services_advisory.py` 选型推荐(Phase 1)
- `tests/test_routers_adrs.py`    ADR 路由(Phase 1)

约定:
- 文件名 `test_*.py`,pytest 自动发现
- 不在本包写业务代码,只放测试用例 + fixtures
- conftest.py 在根目录,提供共享 fixture(app/client/db)
"""
