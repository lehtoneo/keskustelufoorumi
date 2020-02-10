from application import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String, nullable=False)
    
