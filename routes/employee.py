from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_

from models.employee import Employee
from models.designation import Designation
from models.department import Department
from extensions import db

employee = Blueprint(
    "employee",
    __name__,
    url_prefix="/employees"
)


@employee.route("/")
def employee_list():

    search = request.args.get("search", "")

    if search:
        employees = Employee.query.filter(
            or_(
                Employee.employee_name.like(f"%{search}%"),
                Employee.employee_code.like(f"%{search}%"),
                Employee.cnic.like(f"%{search}%")
            )
        ).all()
    else:
        employees = Employee.query.all()

    return render_template(
        "employees/list.html",
        employees=employees,
        search=search
    )


@employee.route("/add", methods=["GET", "POST"])
def add_employee():

    designations = Designation.query.all()

    if request.method == "POST":

        



        emp = Employee(
    employee_code=request.form["employee_code"],
    employee_name=request.form["employee_name"],
    father_name=request.form["father_name"],
    cnic=request.form["cnic"],
    gender=request.form["gender"],
    date_of_birth=request.form.get("date_of_birth") or None,

    phone=request.form["phone"],
    alternate_phone=request.form.get("alternate_phone"),

    email=request.form["email"],

    address=request.form["address"],
    permanent_address=request.form.get("permanent_address"),
    domicile_district=request.form.get("domicile_district"),

    joining_date=request.form.get("joining_date") or None,

    current_salary=request.form.get("current_salary") or None,

    marital_status=request.form.get("marital_status"),
    blood_group=request.form.get("blood_group"),

    status=request.form["status"],

    designation_id=int(request.form.get("designation_id")),
    department_id=int(request.form.get("department_id")),

    supervisor_id=int(request.form.get("supervisor_id"))
    if request.form.get("supervisor_id")
    else None
)





        db.session.add(emp)
        db.session.commit()

        return redirect(
            url_for("employee.employee_list")
        )

    return render_template(
        "employees/add.html",
        designations=designations,
        departments=Department.query.all(),
        employees=Employee.query.all()
    )


@employee.route("/view/<int:employee_id>")
def view_employee(employee_id):

    emp = Employee.query.get_or_404(employee_id)

    return render_template(
        "employees/view.html",
        emp=emp
    )
   
     


@employee.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):

    emp = Employee.query.get_or_404(employee_id)

    if request.method == "POST":
        emp.employee_name = request.form["employee_name"]
        emp.phone = request.form["phone"]

        db.session.commit()

        return redirect(
            url_for("employee.list_employees")
        )

    return render_template(
        "employee/edit.html",
        emp=emp
    )


@employee.route("/delete/<int:employee_id>")
def delete_employee(employee_id):

    emp = Employee.query.get_or_404(employee_id)

    db.session.delete(emp)
    db.session.commit()

    return redirect(
        url_for("employee.list_employees")
    )