from application import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def findChoices():
        init = Category.query.all()
        table = []
        for category in init:
            table.append((str(category.id), str(category.name)))
        
        return table

    