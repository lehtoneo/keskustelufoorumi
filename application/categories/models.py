from application import db
from sqlalchemy.sql import text

from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    threads = relationship("Thread_Category", back_populates="category")

    def __init__(self, name):
        self.name = name

    @staticmethod
    def findChoices(other):
        init = Category.query.all()
        table = []
        for category in init:
            table.append((str(category.id), str(category.name)))
        if other is True:
            table.append(('other', 'other'))
        else:
            table.insert(0, ('All', 'All'))
        return table

    @staticmethod
    def most_common_categories():
        stmt = text('SELECT name, COUNT(category.id) AS count FROM category'
                     ' INNER JOIN "Thread_Category" ON (category.id == "Thread_Category".category_id)'
                     ' GROUP BY category.id'
                     ' ORDER BY count DESC')
        res = db.engine.execute(stmt)

        
        table = []
        for row in res:
            print(row[1])
            rank = len(table) + 1
            table.append({"name":row[0], "count":row[1], "rank":rank})
        

        return table