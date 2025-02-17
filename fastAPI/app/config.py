from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    supabase_url: str
    supabase_key: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    mail_username: str
    mail_password: str
    mail_from: str
    class Config:
        env_file = ".env"

settings = Setting()
