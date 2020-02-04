from application import db
from sqlalchemy.sql import text

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    comment_text = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

    def __init__(self, comment_text):
        self.comment_text = comment_text
        


    @staticmethod
    def connect_users_and_comments(threadid):
        

        # this is not safe, but only way i could make it work both locally and on heroku

        help = "SELECT username, comment_text, posted FROM User INNER JOIN Comment on user_id = user.id WHERE (thread_id = " + threadid + ");"
        stmt = text(help)
        
        res = db.engine.execute(stmt)

        
        
        table = []
        for row in res:
            table.append({"username":row[0], "comment_text":row[1] ,"posted":row[2]})

        return table

        