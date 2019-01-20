import psycopg2
from Instance.config import app_config


def init_db():
    try:
        conn = psycopg2.connect(database='postgres',user='postgres',
        host='localhost',password='12345',port=5433)
        print('databases connected')
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
            public_id VARCHAR (100),
            firstname VARCHAR (30) NOT NULL,
            lastname VARCHAR (30) NOT NULL,
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

