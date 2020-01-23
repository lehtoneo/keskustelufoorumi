from application import app, db
from flask import redirect, render_template, request, url_for
from application.threads.models import Thread
from datetime import datetime


@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())



@app.route("/threads/edit/<thread_id>/", methods=["POST"])
def threads_edit(thread_id):

    return redirect(url_for('threads_openedit', thread_id = thread_id))

@app.route("/threads/edit/<thread_id>", methods=["GET"])
def threads_openedit(thread_id):
    thread = Thread.query.get(thread_id)
    return render_template("threads/edit.html", thread = thread)

@app.route("/threads/edit/<thread_id>/conf", methods=["POST"])
def threads_confirmedit(thread_id):
    thread = Thread.query.get(thread_id)
    thread.title = request.form.get("title")
    thread.modified = datetime.now().replace(microsecond=0)
    db.session().commit()

    return redirect(url_for("threads_index"))




@app.route("/threads/new")
def threads_form():
    return render_template("threads/new.html")

@app.route("/threads", methods=["POST"])
def threads_create():
    thread = Thread(request.form.get("title"))

    db.session().add(thread)
    db.session().commit()

    return redirect(url_for("threads_index"))