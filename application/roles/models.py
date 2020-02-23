from application import db
from sqlalchemy.orm import relationship

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String, nullable=False)
    users = relationship("User_Role", back_populates="role")
    def __init__(self, role):
        self.role = role

class User_Role(db.Model):
    __tablename__ = "User_Role"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id