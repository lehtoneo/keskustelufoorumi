from application import db
from sqlalchemy.sql import text

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    

    def __init__(self, title):
        self.title = title

    @staticmethod
    def connect_threads_and_categories():
        stmt = text('SELECT thread.title AS title, thread."user_id" AS "user_id", thread.posted AS posted, category.name AS category, "user".username AS username, thread.id AS id FROM Thread'
                     ' INNER JOIN Category ON (thread.category_id = category.id)'
                     ' INNER JOIN "user" On (thread."user_id" = "user".id);')
        
        res = db.engine.execute(stmt)
        
        
        table = []
        for row in res:
            print("???")
            table.append({"title":row[0], "user_id":row[1], "posted":row[2], "category":row[3], "username":row[4], "id":row[5]})
        print(table)
        return table