from app.backend.main.src.core.configs.Settings import settings
from .Database import Database as Database


db = Database(settings.postgres.postgres_url, echo=False)
