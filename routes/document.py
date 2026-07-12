from flask import Blueprint, render_template, request, redirect, url_for
from models.document import Document
from models.employee import Employee
from extensions import db

document = Blueprint(
    "document",
    __name__,
    url_prefix="/documents"
)


@document.route("/")
def document_list():

    documents = Document.query.all()

    return render_template(
        "documents/list.html",
        documents=documents
    )


@document.route("/add", methods=["GET", "POST"])
def add_document():

    employees = Employee.query.all()

    if request.method == "POST":

        doc = Document(
            employee_id=request.form["employee_id"],
            document_type=request.form["document_type"],
            file_path=request.form["file_path"],
            notes=request.form["notes"]
        )

        db.session.add(doc)
        db.session.commit()

        return redirect(
            url_for("document.document_list")
        )

    return render_template(
        "documents/add.html",
        employees=employees
    )
