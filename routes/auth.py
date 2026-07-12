from flask import Blueprint, render_template
from flask import request, redirect
from flask import url_for, session

from models.employee import Employee
from models.designation import Designation
from models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(
            username=username,
            password=password,
            status="Active"
        ).first()

        if user:

            session["user_id"] = user.user_id
            session["username"] = user.username
            session["full_name"] = user.full_name
            session["role"] = user.role

            return redirect(
                url_for("auth.dashboard")
            )

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


@auth.route("/dashboard")
def dashboard():

    total_employees = Employee.query.count()

    total_designations = Designation.query.count()

    active_employees = Employee.query.filter_by(
        status="Active"
    ).count()

    return render_template(
        "dashboard/dashboard.html",
        total_employees=total_employees,
        total_designations=total_designations,
        active_employees=active_employees
    )


@auth.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("auth.login")
    )