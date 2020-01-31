from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.threads.models import Thread
from datetime import datetime
from application.threads.forms import NewThreadForm
from application.threads.forms import EditThreadForm

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.query.all())



@app.route("/threads/edit/<thread_id>")
@login_required
def threads_openedit(thread_id):
    thread = Thread.query.get(thread_id)
    
    return render_template("threads/edit.html", thread = thread, form = EditThreadForm())

@app.route("/threads/edit/<thread_id>/conf", methods=["POST"])
@login_required
def threads_confirmedit(thread_id):
    thread = Thread.query.get(thread_id)
    form = EditThreadForm(request.form)

    if not form.validate():
        return render_template("threads/edit.html", thread = thread, form = form)


    
    thread.title = form.title.data
    thread.modified = datetime.now().replace(microsecond=0).replace(second=0)
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/threads/edit/<thread_id>/delete", methods=["POST"])
@login_required
def threads_delete(thread_id):
    Thread.query.filter_by(id=thread_id).delete()
    db.session().commit()
    return redirect(url_for('threads_index'))



@app.route("/threads/new")
@login_required
def threads_form():
    return render_template("threads/new.html", form = NewThreadForm())

@app.route("/threads", methods=["POST"])
@login_required
def threads_create():
    form = NewThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form = form)


    thread = Thread(form.title.data)
    thread.user_id = current_user.id
    db.session().add(thread)
    db.session().commit()

    return redirect(url_for("threads_index"))