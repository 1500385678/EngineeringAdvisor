"""领域模型层。

Pydantic schemas(请求/响应 DTO),与 ORM/数据库模型严格分离:
- `schemas.py`  基础 DTO(本阶段)
- `domain.py`   领域模型(后续 phase 1+ 启用,接 Neo4j/PG 时落地)

约定:DTO 命名以业务语义为准,不带 `Dto`/`Schema` 后缀。
"""
