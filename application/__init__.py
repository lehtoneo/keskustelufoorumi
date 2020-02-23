from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

# Database
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forum.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)



# Log in
from os import urandom
app.config["SECRET_KEY"] = urandom(32)


from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.getRoles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

from application import views

from application.threads import models
from application.threads import views
from application.comments import models

from application.customsearch import views

from application.categories import models
from application.categories.models import Category

from application.roles import models
from application.roles.models import Role, User_Role

from application.auth import models
from application.auth import views

from application.statistics import views

from application.auth.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from sqlalchemy.sql import text
# Create db tables if they don't exist
def init_categories():
    
    stmt = text('SELECT * FROM Category;')
        
    res = db.engine.execute(stmt)
    
    if(res.fetchone() != None):
        return

    category1 = Category('Sports')
    category2 = Category('Gaming')
    category3 = Category('Programming')

    userrole = Role('USER')
    adminrole = Role('ADMIN')

    db.session().add(userrole)
    db.session().add(adminrole)

    db.session().add(category1)
    db.session().add(category2)
    db.session().add(category3)
    db.session().commit()

    normaluser = User(' ', 'user', 'user')
    adminuser = User(' ', 'admin', 'admin')
    
    db.session().add(normaluser)
    db.session().add(adminuser)
    db.session().commit()

    db.session().add(User_Role(normaluser.id, 1))
    db.session().add(User_Role(adminrole.id, 2))
    db.session().commit()






db.create_all()
init_categories()