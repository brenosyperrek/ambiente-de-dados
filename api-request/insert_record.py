import psycopg2
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from request_weather import fetch_data

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="postgres",
            user="airflow",
            password="casan0195"
        )
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise
    
def create_table(conn):
    print("Criando tabela raw_weather_data se não existir...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;                     
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("Tabela raw_weather_data criada ou já existente.")
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela raw_weather_data: {e}")
        raise

def insert_records(conn, data):
    print("Inserindo registros na tabela raw_weather_data...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city, 
                temperature, 
                weather_description, 
                wind_speed, 
                time,
                inserted_at, 
                utc_offset)
            VALUES (%s, %s, %s, %s, %s, NOW(), %s);
        """, (
            data['name'],
            data['main']['temp'] - 273.15,
            data['weather'][0]['description'],
            data['wind']['speed'],
            datetime.fromtimestamp(data['dt']),
            data['timezone'] / 3600 
        ))
        conn.commit()
        print("Registros inseridos com sucesso na tabela raw_weather_data.")
    except psycopg2.Error as e:
        print(f"Erro ao inserir registros na tabela raw_weather_data: {e}")
        raise

def main():
    try:
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"Erro no processo principal: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Conexão com o banco de dados fechada.")
            
main()