from flask import render_template
from application import app, db
from sqlalchemy import desc

from application.threads.models import Thread, Thread_Category

@app.route("/")
def index():
    threads = Thread.query.order_by(desc(Thread.posted)).limit(3).all()
    return render_template("index.html", threads = threads)