from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATOS DE TU MYSQL
MYSQL_USER = "root"
MYSQL_PASSWORD = ""     # tu contraseña si tienes
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = "3306"
MYSQL_DB = "notas_db"

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

engine = create_engine(
    DATABASE_URL,
    echo=True  # Muestra información en consola (puede quitarse)
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()
