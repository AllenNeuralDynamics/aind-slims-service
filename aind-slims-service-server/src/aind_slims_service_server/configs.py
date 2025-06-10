"""Module for settings to connect to SLIMS backend"""

from aind_settings_utils.aws import (
    ParameterStoreAppBaseSettings,
)
from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict


class Settings(ParameterStoreAppBaseSettings):
    """Settings for connecting to SLIMS Database."""

    username: str = Field(..., description="User name")
    password: SecretStr = Field(..., description="Password")
    host: str = Field(..., description="host")
    db: str = Field(default="slims", description="Database")
    model_config = SettingsConfigDict(
        env_prefix="SLIMS_",
        case_sensitive=False,
    )
