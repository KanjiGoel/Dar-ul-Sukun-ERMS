from flask import Blueprint, render_template
from models.employee import Employee
from models.department import Department
from models.designation import Designation

dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)

@dashboard.route("/")
def home():

    total_employees = Employee.query.count()

    active_employees = Employee.query.filter_by(
        status="Active"
    ).count()

    inactive_employees = Employee.query.filter_by(
        status="Inactive"
    ).count()

    total_departments = Department.query.count()

    total_designations = Designation.query.count()

    return render_template(
        "dashboard/index.html",
        total_employees=total_employees,
        active_employees=active_employees,
        inactive_employees=inactive_employees,
        total_departments=total_departments,
        total_designations=total_designations
    )