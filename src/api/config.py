from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    DATABASE_NAME: str = "./todo_app.db"
    SQLALCHEMY_DATABASE_URL: str = f"sqlite+aiosqlite:///{DATABASE_NAME}"


class TestingSettings(BaseSettings):
    DATABASE_NAME: str = "./test.db"
    SQLALCHEMY_DATABASE_URL: str = f"sqlite+aiosqlite:///{DATABASE_NAME}"


settings = Settings()
testing_settings = TestingSettings()
