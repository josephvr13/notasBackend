import sqlalchemy
from sqlalchemy import text
from sqlalchemy.engine import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

sql_script = """
CREATE TABLE IF NOT EXISTS notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    contenido TEXT NOT NULL,
    creado_en DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO notas (titulo, contenido) VALUES
('Recordatorio', 'Comprar comida para el perro antes del viernes.'),
('Idea de proyecto', 'Crear una app para gestionar notas con FastAPI y MySQL.'),
('Tarea pendiente', 'Terminar el informe del proyecto de tecnología.'),
('Cita médica', 'Consulta general el lunes a las 9:00 AM.'),
('Lista de compras', 'Arroz, leche, huevos, carne, café.'),
('Aprendizaje', 'Investigar cómo funcionan los modelos ORM en SQLAlchemy.'),
('Objetivo semanal', 'Completar al menos 10 horas de estudio.'),
('Plan de viaje', 'Visitar Medellín en enero, reservar hotel.'),
('Reunión', 'Reunión con el instructor sobre avances del proyecto.'),
('Recordar', 'Hacer copia de seguridad del backend del proyecto.');
"""

with engine.connect() as conn:
    print("Ejecutando script SQL...")
    conn.execute(text(sql_script))
    conn.commit()
    print("Base de datos inicializada correctamente.")
