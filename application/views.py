from flask import render_template
from flask_login import current_user
from application import app, db
from sqlalchemy import desc

from application.threads.models import Thread, Thread_Category

@app.route("/")
def index():
    threads = Thread.query.order_by(desc(Thread.posted)).limit(3).all()
    admin = False
    if current_user.is_authenticated:
        if "ADMIN" in current_user.getRoles():
            admin = True
    return render_template("index.html", threads = threads, admin = admin)