from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user


from application.threads.models import Thread
from application.auth.models import User
from application.categories.models import Category

@app.route("/basicstats", methods=["GET"])
def stats_open():
    mostactive = User.most_active_users_threads()
    mostcommoncategories = Category.most_common_categories()
    return render_template("statistics/basicstats.html", mostactive = mostactive, mostcommon = mostcommoncategories)