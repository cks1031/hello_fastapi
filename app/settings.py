from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    userid = ''
    passwd = ''
    dbname = 'clouds2024'
    dburl = ''
    sqlite_url = f'sqlite:///app/{dbname}.db'

config = Settings()