from datetime import datetime
import psycopg2
from app.api.v2.utils.database import init_db


class Question(object):

    def __init__(self, *args):
        self.meetup_id = args[0]
        self.username = args[1]
        self.title = args[2]
        self.body = args[3]
        self.db = init_db()

    def add_quiz (self):
        new_quiz = {
            'meetup_id': self.meetup_id,
            'username': self.username,
            "title": self.title,
            "body": self.body
        }
        try:
            query = """
                    INSERT INTO questions(meetup_id, created_by, title,body,votes) 
                    VALUES (%(meetup_id)s, %(username)s, %(title)s,%(body)s,0
                    ) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_quiz)
            self.db.commit()
            return new_quiz
        except (Exception, psycopg2.Error) as error:
            print(error)