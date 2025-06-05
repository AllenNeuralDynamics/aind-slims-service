"""Module for settings to connect to SLIMS backend"""

import os

from aind_settings_utils.aws import (
    ParameterStoreAppBaseSettings,
)
from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict


class Settings(ParameterStoreAppBaseSettings):
    """Settings for connecting to SLIMS Database."""

    model_config = SettingsConfigDict(
        env_prefix="SLIMS_",
        extra="ignore",
        aws_param_store_name=os.getenv("AWS_PARAM_STORE_NAME"),
    )

    username: str = Field(..., description="User name")
    password: SecretStr = Field(..., description="Password")
    host: str = Field(..., description="host")
    db: str = Field(default="slims", description="Database")
