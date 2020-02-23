from application import app, db
from flask import redirect, render_template, request, url_for
from sqlalchemy import asc, desc

from application.threads import views as threadviews
from application.threads.models import Thread

from application.customsearch.forms import DateForm
from application.categories.forms import CategoryForm


@app.route("/threads/customsearch", methods=["GET"])
def customsearch_open():
    dateform = DateForm()
    
    return render_template("customsearch/customsearch.html", dateform = dateform, categoryform = CategoryForm(None, False))

@app.route("/threads/customsearch", methods=["POST"])
def customsearch_search():
    dateform = DateForm(request.form)
    categoryform = CategoryForm(request.form, False)
    newest = (dateform.radios.data == 'newest')
    
    return customsearch_search_with_parameters(categoryform.categories.data, newest)

@app.route("/threads/customsearch/search", methods=["GET"])
def customsearch_search_with_parameters(category_id, newest):

    if category_id == 'All':

        if newest:
            threads = Thread.query.order_by(desc(Thread.posted)).all()
        else:
            threads = Thread.query.order_by(asc(Thread.posted)).all()

    else:
        if newest:
            threads = Thread.query.order_by(desc(Thread.posted)).filter(Thread.categories.any(category_id=category_id)).all()
        else:
            threads = Thread.query.order_by(asc(Thread.posted)).filter(Thread.categories.any(category_id=category_id)).all()

    return threadviews.threads_with_customsearch(threads)



