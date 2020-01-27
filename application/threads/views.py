from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.threads.models import Thread
from datetime import datetime
from application.threads.forms import ThreadForm

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())



@app.route("/threads/edit/<thread_id>/", methods=["POST"])
@login_required
def threads_edit(thread_id):

    return redirect(url_for('threads_openedit', thread_id = thread_id))

@app.route("/threads/edit/<thread_id>", methods=["GET"])
@login_required
def threads_openedit(thread_id):
    thread = Thread.query.get(thread_id)
    return render_template("threads/edit.html", thread = thread)

@app.route("/threads/edit/<thread_id>/conf", methods=["POST"])
@login_required
def threads_confirmedit(thread_id):
    thread = Thread.query.get(thread_id)
    thread.title = request.form.get("title")
    thread.modified = datetime.now().replace(microsecond=0)
    db.session().commit()

    return redirect(url_for("threads_index"))




@app.route("/threads/new")
@login_required
def threads_form():
    return render_template("threads/new.html", form = ThreadForm())

@app.route("/threads", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form = form)


    thread = Thread(form.title.data)

    db.session().add(thread)
    db.session().commit()

    return redirect(url_for("threads_index"))