from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Wildberries Products Parser'
    app_description: str = (
        'App for parsing and storing information about Wildeberries products'
    )
    db_url: str = 'postgresql+asyncpg://user:password@localhost/products.db'

    class Config:
        env_file = '.env'


settings = Settings()
