from application import app, db, login_required
from flask import redirect, render_template, request, url_for

from flask_login import current_user
from application.comments.models import Comment
from application.comments.forms import CommentForm
from application.auth.models import User
from application.threads.models import Thread
from datetime import datetime
from application.threads.forms import NewThreadForm
from application.threads.forms import EditThreadTitleForm, EditThreadDescriptionForm

@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads = Thread.connect_threads_and_categories())

@app.route("/threads/read/<thread_id>", methods=["POST"])
@login_required
def threads_comment(thread_id):
    form = CommentForm(request.form)
    
    if not form.validate():
        thread = Thread.query.get(thread_id)
        comments = Comment.connect_users_and_comments(thread_id)
        user = User.query.get(thread.user_id)
        return render_template("threads/showthread.html", form = form, comments = comments, thread = thread, user = user)

    comment = Comment(form.comment.data)
    comment.thread_id = thread_id
    comment.user_id = current_user.id
    db.session().add(comment)
    db.session().commit()

    return threads_open(thread_id)

@app.route("/threads/read/<thread_id>", methods=["GET"])
def threads_open(thread_id):
    thread = Thread.query.get(thread_id)
    comments = Comment.connect_users_and_comments(thread_id)

    
    
    return render_template("threads/showthread.html", form = CommentForm(), comments = comments, thread = thread, user = thread.user)

@app.route("/threads/edit/<thread_id>")
@login_required
def threads_openedit(thread_id):
    thread = Thread.query.get(thread_id)
    if(thread.user_id != current_user.id):
        return threads_openmythreads()
    return render_template("threads/edit.html", thread = thread, titleform = EditThreadTitleForm(), descform = EditThreadDescriptionForm())

@app.route("/threads/edit/<thread_id>/conf_title", methods=["POST"])
@login_required
def threads_confirm_title_edit(thread_id):
    thread = Thread.query.get(thread_id)
    titleform = EditThreadTitleForm(request.form)
    print(titleform.validate())
    if not titleform.validate():
        
        return render_template("threads/edit.html", thread = thread, titleform = titleform, descform = EditThreadDescriptionForm())


    
    thread.title = titleform.title.data
    thread.modified = datetime.now().replace(microsecond=0).replace(second=0)
    db.session().commit()

    return threads_open(thread_id)

@app.route("/threads/edit/<thread_id>/conf_description", methods=["POST"])
@login_required
def threads_confirm_description_edit(thread_id):
    thread = Thread.query.get(thread_id)
    descform = EditThreadDescriptionForm(request.form)
    if not descform.validate():
        
        return render_template("threads/edit.html", thread = thread, titleform = EditThreadTitleForm, descform = descform)


    
    thread.description = descform.description.data
    thread.modified = datetime.now().replace(microsecond=0).replace(second=0)
    db.session().commit()

    return threads_open(thread_id)


@app.route("/threads/edit/<thread_id>/delete", methods=["POST"])
@login_required
def threads_delete(thread_id):
    
    Comment.query.filter_by(thread_id=thread_id).delete()
    db.session().commit()
    Thread.query.filter_by(id=thread_id).delete()
    db.session().commit()
    return redirect(url_for('threads_index'))

@app.route("/threads/deletecomment/<comment_id>", methods=["POST"])
@login_required
def comment_delete(comment_id):
    Comment.query.filter_by(id=comment_id).delete()
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
    thread.description = form.description.data
    thread.category_id = int(form.categories.data)
    
    
    db.session().add(thread)
    db.session().commit()

    return redirect(url_for("threads_index"))

@app.route("/threads/mythreads")
@login_required
def threads_openmythreads():
    user = current_user
    ownthreads = Thread.query.filter_by(user_id=user.id)
    

    return render_template("threads/mythreads.html", ownthreads = ownthreads)