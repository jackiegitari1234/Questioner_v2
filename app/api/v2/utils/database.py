import psycopg2
import os
from Instance.config import app_config


config = os.getenv("FLASK_ENV")


def init_db():
    try:
        if config == "development":
            db_url = os.getenv("DATABASE_URL")
        else:
            # db_url = os.getenv("TEST_DATABASE_URL")
            db_url = "dbname='testingdb' host='127.0.0.1' port='5432' user='postgres' password='12345'"
        conn = psycopg2.connect(db_url)
        conn.commit()
        print (config)
        return conn    
    except (Exception, psycopg2.Error) as error:
        print("Unable to connect to the database", error)
     

def create_tables():

    try:
        conn = init_db()
        cursor = conn.cursor()
        member = ''' 
            CREATE TABLE IF NOT EXISTS member (
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
        
        meetup = """
            CREATE TABLE IF NOT EXISTS meetups(
            id SERIAL PRIMARY KEY,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            topic VARCHAR (50) NOT NULL,
            location VARCHAR (20) NOT NULL,
            happeningOn VARCHAR (20) NOT NULL,
            tags VARCHAR (20) NOT NULL
        );
        """
        rsvps = """
            CREATE TABLE IF NOT EXISTS rsvp(
            id SERIAL PRIMARY KEY,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            meetup_id VARCHAR (50) NOT NULL,
            username VARCHAR (20) NOT NULL,
            response VARCHAR (20) NOT NULL
        );
        """
        questions = """
            CREATE TABLE IF NOT EXISTS questions(
            id SERIAL PRIMARY KEY,
            meetup_id VARCHAR (50) NOT NULL,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            created_by VARCHAR (20) NOT NULL,
            title VARCHAR (20) NOT NULL,
            body VARCHAR (20) NOT NULL,
            votes VARCHAR (20) NOT NULL
        );
        """
        comment = """
            CREATE TABLE IF NOT EXISTS comments(
            id SERIAL PRIMARY KEY,
            question_id VARCHAR (50) NOT NULL,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            created_by VARCHAR (20) NOT NULL,
            body VARCHAR (20) NOT NULL
        );
        """
        votes = """
            CREATE TABLE IF NOT EXISTS votes(
            id SERIAL PRIMARY KEY,
            question_id VARCHAR (50) NOT NULL,
            created_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            created_by VARCHAR (20) NOT NULL,
            status VARCHAR (20) NOT NULL
        );
        """
        all_queries = [member, meetup, rsvps, questions, comment, votes]
        for each_query in all_queries:
            cursor.execute(each_query)
        conn.commit()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print("Unable to create tables", error)


def drop_all_tables():
    connec = init_db()
    print("config")
    cursor = connec.cursor()
    cursor.execute("DROP TABLE IF EXISTS member CASCADE")
    
    connec.commit()
    connec.close()

