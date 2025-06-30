#PostgreSQL connect, insert, fetch functions
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="face_db",
    user="postgres",
    password="7922"
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        face_encoding BYTEA NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

cur.close()
conn.close()