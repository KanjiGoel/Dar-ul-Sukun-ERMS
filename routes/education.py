from flask import Blueprint, render_template, request, redirect, url_for
from models.education import Education
from models.employee import Employee
from extensions import db

education = Blueprint(
    "education",
    __name__,
    url_prefix="/education"
)

@education.route("/")
def education_list():
    educations = Education.query.all()
    return render_template(
        "education/list.html",
        educations=educations
    )

@education.route("/add", methods=["GET", "POST"])
def add_education():

    employees = Employee.query.all()

    if request.method == "POST":

        edu = Education(
    employee_id=request.form["employee_id"],
    degree=request.form["degree_name"],
    institute_name=request.form["institute"],
    passing_year=request.form["year"]
)

        db.session.add(edu)
        db.session.commit()

        return redirect(
            url_for("education.education_list")
        )

    return render_template(
        "education/add.html",
        employees=employees
    )