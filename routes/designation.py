from flask import Blueprint, render_template, request, redirect, url_for
from models.designation import Designation
from extensions import db

designation = Blueprint("designation", __name__)


@designation.route("/designation")
def list_designations():
    designations = Designation.query.all()

    return render_template(
        "designation/list.html",
        designations=designations
    )


@designation.route("/edit/<int:designation_id>", methods=["GET", "POST"])
def edit_designation(designation_id):

    d = Designation.query.get_or_404(designation_id)

    if request.method == "POST":
        d.designation_name = request.form["designation_name"]

        db.session.commit()

        return redirect(
            url_for("designation.list_designations")
        )

    return render_template(
        "designation/edit.html",
        designation=d
    )


@designation.route("/delete/<int:designation_id>")
def delete_designation(designation_id):

    d = Designation.query.get_or_404(designation_id)

    db.session.delete(d)
    db.session.commit()

    return redirect(
        url_for("designation.list_designations")
    )



@designation.route("/add", methods=["GET", "POST"])
def add_designation():

    if request.method == "POST":

        new_designation = Designation(
            designation_name=request.form["designation_name"],
            description=request.form.get("description"),
            basic_salary=request.form["basic_salary"],
            status=request.form["status"]
        )

        db.session.add(new_designation)
        db.session.commit()

        return redirect(
            url_for("designation.list_designations")
        )

    return render_template(
        "designation/add.html"
    )
    