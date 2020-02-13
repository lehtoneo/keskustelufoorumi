from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "user"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(5), nullable=False)

    threads = db.relationship("Thread", backref="user")

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if(self.role == "ADMIN"):
            return ["ADMIN"]
        return ["USER"]

    @staticmethod
    def most_active_users_threads():
        stmt = text('SELECT username, COUNT("user".id) AS count FROM "user"'
                     ' INNER JOIN Thread ON ("user".id = thread.user_id)'
                     ' GROUP BY "user".id'
                     ' ORDER BY count DESC')
        res = db.engine.execute(stmt)

        
        table = []
        for row in res:
            print(row[1])
            rank = len(table) + 1
            table.append({"username":row[0], "count":row[1], "rank":rank})
        

        return table