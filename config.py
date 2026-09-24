import locust.stats
from pydantic_settings import BaseSettings, SettingsConfigDict

locust.stats.PERCENTILES_TO_REPORT = [0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99, 1.0]
locust.stats.CSV_STATS_INTERVAL_SEC = 5
locust.stats.HISTORY_STATS_INTERVAL_SEC = 5
locust.stats.CONSOLE_STATS_INTERVAL_SEC = 5
locust.stats.CSV_STATS_FLUSH_INTERVAL_SEC = 5


class Settings(BaseSettings):
    base_url: str
    host_port: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
