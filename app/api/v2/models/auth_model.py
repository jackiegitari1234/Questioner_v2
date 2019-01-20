from datetime import datetime
import psycopg2
from app.api.v2.utils.database import init_db

class User(object):

    def __init__(self, *args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.username = args[2]
        self.email = args[3]
        self.password = args[4]
        self.db = init_db()

    def register_user(self):
        new_user = {
            # "public_id": str(uuid.uuid4()),
            'firstname': self.firstname,
            'lastname': self.lastname,
            'isAdmin': False,
            "username": self.username,
            'registered': datetime.now(),
            "email": self.email,
            "password": self.password
        }
        try:
            query = """INSERT INTO USERS(public_id, firstname, lastname, othername, PhoneNumber, isAdmin, registered, username, email, password) 
                    VALUES (%(public_id)s, %(firstname)s, %(lastname)s, %(othername)s, %(PhoneNumber)s, %(isAdmin)s,%(registered)s, %(username)s, %(email)s,%(password)s) """
            cur = self.db.cursor()
            cur.execute(query, new_user)
            self.db.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)
            return {"message": "Not able to insert in users table"}, 400