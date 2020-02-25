from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.comments.models import Comment
from application.comments.forms import CommentForm
from flask_login import current_user

from application.threads import views as threadviews

@app.route("/edit/comment/<comment_id>", methods=["GET"])
@login_required
def comment_edit(comment_id):
    comment = Comment.query.get(comment_id)

    return render_template("comments/editcomment.html", comment = comment, form = CommentForm())

@app.route("/edit/comment/<comment_id>", methods=["POST"])
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