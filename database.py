import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# --- 1. Intentar tomar la URL de la base de datos de Render ---
DATABASE_URL = os.getenv("DATABASE_URL")

# --- 2. Si NO existe (estás trabajando local) usar tu MySQL local ---
if not DATABASE_URL:
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""   # tu contraseña local
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = "3306"
    MYSQL_DB = "notas_db"

    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

# --- 3. Crear engine universal ---
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # Evita errores de desconexión en Render
)

# --- 4. Crear sesión ---
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# --- 5. Base del ORM ---
Base = declarative_base()
