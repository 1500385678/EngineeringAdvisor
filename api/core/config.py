"""配置中心。

Pydantic Settings · 12-factor · 全部从环境变量 + `.env` 加载。
- 默认值仅在本地开发/测试时使用,生产环境必须显式注入。
- 新增配置项请加 `description` 字段,便于 `/docs` 自动展示。
"""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """全局配置单例。"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # 运行模式
    env: Literal["dev", "test", "staging", "prod"] = Field(
        default="dev",
        description="运行环境:dev / test / staging / prod",
    )
    debug: bool = Field(
        default=False,
        description="是否启用 debug(uvicorn reload、详细日志等)",
    )

    # 服务端口(供 `python -m api.main` 或 docker-compose 读取)
    host: str = Field(default="0.0.0.0", description="绑定 host")
    port: int = Field(default=8000, ge=1, le=65535, description="绑定 port")

    # CORS(后续前端联调时启用,目前留空表示全 deny)
    cors_allow_origins: list[str] = Field(
        default_factory=lambda: ["http://localhost:3000"],
        description="允许的跨域来源",
    )

    # 日志级别
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO",
        description="日志级别",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """缓存单例,避免每次请求都重新解析环境变量。"""
    return Settings()


# 导出常用别名,`from api.core.config import settings` 即可
settings = get_settings()
