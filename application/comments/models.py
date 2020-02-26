from application import db
from sqlalchemy.sql import text

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    comment_text = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

    def __init__(self, comment_text):
        self.comment_text = comment_text
        

        