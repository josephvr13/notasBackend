import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Intentar usar la URL de Render
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Si no existe, usar MySQL local
if not DATABASE_URL:
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""   # pon tu clave local si tienes
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = "3306"
    MYSQL_DB = "notas_db"
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # evita desconexiones en Render
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
