from datetime import datetime
import psycopg2
from app.api.v2.utils.database import init_db


class Meetup(object):

    def __init__(self, *args):
        self.topic = args[0]
        self.location = args[1]
        self.happeningOn = args[2]
        self.tags = args[3]
        self.db = init_db()

    def register_meetup(self):
        new_meetup = {
            'topic': self.topic,
            'location': self.location,
            "happeningOn": self.happeningOn,
            "tags": self.tags
        }
        try:
            query = """
                    INSERT INTO meetups(topic, location, happeningOn,tags) 
                    VALUES (%(topic)s, %(location)s, %(happeningOn)s,
                    %(tags)s) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_meetup)
            self.db.commit()
            return new_meetup
        except (Exception, psycopg2.Error) as error:
            print(error)

def check_admin(current_user):
    try:
        cur = init_db().cursor()
        # print(current_user)
        query = "SELECT isAdmin FROM member WHERE username= %s";
        cur.execute(query, (current_user,))
        user_exists = cur.fetchone()
        cur.close()

        details = (user_exists[0])
        print(details)

        if details == True:
            return True
        return False
    except (Exception, psycopg2.Error) as error:
        print(error)
    
 
