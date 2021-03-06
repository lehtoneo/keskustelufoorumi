from application import app, db, login_required
from flask import redirect, render_template, request, url_for

from flask_login import current_user
from application.comments.models import Comment
from application.comments.forms import CommentForm
from application.categories.models import Category
from application.threads.models import Thread, Thread_Category
from application.categories.forms import CategoryForm
from application.threads.forms import NewThreadForm
from application.threads.forms import EditThreadTitleForm, EditThreadDescriptionForm

@app.route("/threads", methods=["GET"])
def threads_index():
    categoryform = CategoryForm(None, False)
    admin = False
    if current_user.is_authenticated:
        if "ADMIN" in current_user.getRoles():
            admin = True

    return render_template("threads/list.html", threads = Thread.query.all(), categoryform = categoryform, admin = admin)

@app.route("/threads/custom", methods=["GET"])
def threads_with_customsearch(threads):
    categoryform = CategoryForm(None, False)
    admin = False
    if current_user.is_authenticated:
        if "ADMIN" in current_user.getRoles():
            admin = True

    return render_template("customsearch/listcustom.html", threads = threads, categoryform = categoryform, admin = admin)

@app.route("/threads/admin/delete/thread/<thread_id>", methods=["POST"])
@login_required(role="ADMIN")
def admin_thread_delete(thread_id):

    Comment.query.filter_by(thread_id=thread_id).delete()
    Thread_Category.query.filter_by(thread_id=thread_id).delete()
    Thread.query.filter_by(id=thread_id).delete()

    db.session().commit()

    return threads_index()


@app.route("/threads/category", methods=["POST"])
def threads_with_category():
    categoryform = CategoryForm(request.form, False)
    if categoryform.categories.data == 'All':
        return threads_index()
    return open_threads_with_category(categoryform.categories.data)

@app.route("/threads/<category_id>", methods=["GET"])
def open_threads_with_category(category_id):
    
    threads = Thread.query.filter(Thread.categories.any(category_id=category_id)).all()
    
    return render_template("threads/list.html", threads = threads, categoryform = CategoryForm(None, False))



@app.route("/threads/read/<thread_id>", methods=["GET"])
def threads_open(thread_id):
    thread = Thread.query.get(thread_id)

    comments = thread.comments

    admin = False
    if current_user.is_authenticated:
        if "ADMIN" in current_user.getRoles():
            admin = True
    
    return render_template("threads/showthread.html", form = CommentForm(), comments = comments, thread = thread, user = thread.user, admin = admin)

@app.route("/threads/edit/<thread_id>")
@login_required
def threads_openedit(thread_id):
    thread = Thread.query.get(thread_id)
    if(thread.user_id != current_user.id):
        return threads_openmythreads()
    return render_template("threads/edit.html", thread = thread, titleform = EditThreadTitleForm(), descform = EditThreadDescriptionForm(), categoryform = CategoryForm(None, True))



@app.route("/threads/new", methods=["GET"])
@login_required
def threads_new():
    categoryform = CategoryForm(None, True)
    return render_template("threads/new.html", threadform = NewThreadForm(), categoryform = categoryform)



@app.route("/threads", methods=["POST"])
@login_required
def threads_create():
    threadform = NewThreadForm(request.form)
    categoryform = CategoryForm(request.form, True)


    if not threadform.validate():
        return render_template("threads/new.html", threadform = threadform, categoryform = categoryform)

    thread = Thread(threadform.title.data)
    thread.user_id = current_user.id
    thread.description = threadform.description.data
    if categoryform.categories.data == 'other':

        if not categoryform.validate():
            return render_template("threads/new.html", threadform = threadform, categoryform = categoryform)

        
        category = Category.query.filter_by(name=categoryform.othercategory.data).first()

        if category:
            categoryform.othercategory.errors.append('Category is already on the list, please select it from there')
            return render_template("threads/new.html", threadform = threadform, categoryform = categoryform)

        newcategory = Category(categoryform.othercategory.data)

        db.session().add(newcategory)
        db.session().commit()
        db.session().add(thread)
        db.session().commit()
        thread_category = Thread_Category(thread.id, newcategory.id)
        db.session().add(thread_category)
        db.session().commit()
        db.session().commit()
        return redirect(url_for("threads_index"))

    db.session().add(thread)
    db.session().commit()
    thread_category = Thread_Category(thread.id, int(categoryform.categories.data))
    db.session().add(thread_category)
    db.session().commit()
    return redirect(url_for("threads_index"))

@app.route("/threads/mythreads")
@login_required
def threads_openmythreads():
    user = current_user
    ownthreads = Thread.query.filter_by(user_id=user.id)
    

    return render_template("threads/mythreads.html", threads = ownthreads)

@app.route("/threads/edit/<thread_id>/addcategory", methods=["POST"])
@login_required
def threads_add_new_category(thread_id):
    categoryform = CategoryForm(request.form, True)
    thread = Thread.query.get(thread_id)
    
    if categoryform.categories.data == 'other':

        if not categoryform.validate():
            return render_template("threads/edit.html", threadform = EditThreadTitleForm(), descform = EditThreadDescriptionForm(),categoryform = categoryform)

        
        category = Category.query.filter_by(name=categoryform.othercategory.data).first()

        if category:
            categoryform.othercategory.errors.append('Category is already on the list, please select it from there')
            return render_template("threads/edit.html", threadform = EditThreadTitleForm(), descform = EditThreadDescriptionForm(),categoryform = categoryform)

        newcategory = Category(categoryform.othercategory.data)
        db.session().add(newcategory)
        db.session().commit()
        thread_category = Thread_Category(thread.id, newcategory.id)
        db.session().add(thread_category)
        db.session().commit()

        return redirect(url_for("threads_index"))

    
    
    
    categories = Category.query.filter(Category.threads.any(thread_id=thread_id)).all()
    for category in categories:
        if(category.id == int(categoryform.categories.data)):
            return redirect(url_for("threads_index"))

    thread_category = Thread_Category(thread.id, int(categoryform.categories.data))
    db.session().add(thread_category)
    db.session().commit()

    return redirect(url_for("threads_index"))

@app.route("/threads/edit/<thread_id>/conf_title", methods=["POST"])
@login_required
def threads_confirm_title_edit(thread_id):
    thread = Thread.query.get(thread_id)

    if(thread.user_id != current_user.id):
        return threads_openmythreads()

    titleform = EditThreadTitleForm(request.form)

    if not titleform.validate():
        
        return render_template("threads/edit.html", thread = thread, titleform = titleform, descform = EditThreadDescriptionForm(), categoryform = CategoryForm(None, False))


    
    thread.title = titleform.title.data
    db.session().commit()

    return threads_open(thread_id)

@app.route("/threads/edit/<thread_id>/conf_description", methods=["POST"])
@login_required
def threads_confirm_description_edit(thread_id):
    thread = Thread.query.get(thread_id)
    if(thread.user_id != current_user.id):
        return threads_openmythreads()
    descform = EditThreadDescriptionForm(request.form)
    if not descform.validate():
        
        return render_template("threads/edit.html", thread = thread, titleform = EditThreadTitleForm(), descform = descform)


    
    thread.description = descform.description.data
    db.session().commit()

    return threads_open(thread_id)



@app.route("/threads/edit/<thread_id>/delete", methods=["POST"])
@login_required
def threads_delete(thread_id):
    thread = Thread.query.get(thread_id)
    if(thread.user_id != current_user.id):
        return threads_openmythreads()
    Comment.query.filter_by(thread_id=thread_id).delete()
    Thread_Category.query.filter_by(thread_id=thread_id).delete()
    Thread.query.filter_by(id=thread_id).delete()
    db.session().commit()
    return threads_openmythreads()
