from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

class Thread(db.Model):
    __tablename__ = 'thread'
    id = db.Column(db.Integer, primary_key=True)

    posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    categories = relationship("Thread_Category", back_populates="thread")
    comments = db.relationship("Comment", backref="thread")

    def __init__(self, title):
        self.title = title


class Thread_Category(db.Model):
    __tablename__ = 'Thread_Category'
    thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)
    
    category = relationship("Category", back_populates="threads")
    thread = relationship("Thread", back_populates="categories")

    def __init__(self, thread_id, category_id):
        self.thread_id = thread_id
        self.category_id = category_id

    