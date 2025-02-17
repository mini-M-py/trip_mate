from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from supabase import create_client, Client

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}?sslmode=require'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
supabase: Client = create_client(settings.supabase_url,settings.supabase_key)

SessionLocal = sessionmaker(autocommit =False, autoflush= False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
