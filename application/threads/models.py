from application import db

class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified = db.Column(db.DateTime, default=db.func.current_timestamp())
    onupdate = db.func.current_timestamp()

    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    category = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title):
        self.title = title