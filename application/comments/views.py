from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.threads.models import Thread
from application.comments.models import Comment
from application.comments.forms import CommentForm
from flask_login import current_user

from application.threads import views as threadviews

@app.route("/comment/edit/<comment_id>", methods=["GET"])
@login_required
def comment_edit(comment_id):
    comment = Comment.query.get(comment_id)

    return render_template("comments/editcomment.html", comment = comment, form = CommentForm())

@app.route("/comment/edit/<comment_id>", methods=["POST"])
@login_required
def comment_edit_post(comment_id):
    comment = Comment.query.get(comment_id)
    if(current_user.id != comment.user_id):
        return threadviews.threads_index()
    form = CommentForm(request.form)
    
    if not form.validate():
        return render_template("comments/editcomment.html", comment = comment, form = form)
    
    comment.comment_text = form.comment.data
    db.session().commit()
    return threadviews.threads_open(comment.thread_id)

@app.route("/comment/<thread_id>", methods=["POST"])
@login_required
def comment_post(thread_id):
    form = CommentForm(request.form)
    
    if not form.validate():
        thread = Thread.query.get(thread_id)
        comments = thread.comments
        
        return render_template("threads/showthread.html", form = form, comments = comments, thread = thread, user = thread.user)

    comment = Comment(form.comment.data)
    comment.thread_id = thread_id
    comment.user_id = current_user.id
    db.session().add(comment)
    db.session().commit()

    return threadviews.threads_open(thread_id)

@app.route("/comment/deletecomment/<comment_id>", methods=["POST"])
@login_required
def comment_delete(comment_id):
    comment = Comment.query.get(comment_id)
    threadid = comment.thread_id
    if(comment.user_id != current_user.id):
        return threadviews.threads_open(threadid)
    Comment.query.filter_by(id=comment_id).delete()
    db.session().commit()

    return threadviews.threads_open(threadid)

@app.route("/comment/admin/delete/comment/<comment_id>", methods=["POST"])
@login_required(role="ADMIN")
def admin_comment_delete(comment_id):

    comment = Comment.query.get(comment_id)
    threadid = comment.thread_id

    Comment.query.filter_by(id=comment_id).delete()
    db.session().commit()


    return threadviews.threads_open(threadid)