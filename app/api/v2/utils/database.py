import psycopg2,os
from Instance.config import app_config


config = os.getenv("FLASK_ENV")

def init_db():
    try:
        if config == "development":
            db_url = os.getenv("DATABASE_URL")
        else:
            db_url="dbname='testingdb' host='127.0.0.1' port='5433' user='postgres' password='12345'"
        conn = psycopg2.connect(db_url)
        print('database connected')
        conn.commit()
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Unable to connect to the database", error)


def create_tables():
    
    
    try:
        conn = init_db()
        cursor = conn.cursor()
        query = ''' CREATE TABLE IF NOT EXISTS member (
            id serial PRIMARY KEY,
            public_id VARCHAR (50),
            firstname VARCHAR (40) NOT NULL,
            lastname VARCHAR (40) NOT NULL,
            othername VARCHAR (30) NOT NULL,
            username VARCHAR (30) NOT NULL,
            registered DATE NOT NULL,
            email VARCHAR (30) UNIQUE NOT NULL,
            PhoneNumber VARCHAR NOT NULL,
            isAdmin BOOLEAN NOT NULL DEFAULT FALSE,
            password VARCHAR (200) NOT NULL
                
        );
        '''
        cursor.execute(query)
        conn.commit()
        cursor.close()
        
        print("successfully created")
    except (Exception, psycopg2.Error) as error:
        print("Unable to create tables", error)

def drop_all_tables():
    connec = init_db()
    cursor = connec.cursor()
    cursor.execute("DROP TABLE IF EXISTS member CASCADE")
    connec.commit()
    cursor.close()

