from extensions import db

class Employee(db.Model):
    __tablename__ = "employees"

    employee_id = db.Column(db.Integer, primary_key=True)

    employee_code = db.Column(db.String(50))

    employee_name = db.Column(db.String(120), nullable=False)

    father_name = db.Column(db.String(120))

    cnic = db.Column(db.String(15), unique=True)

    gender = db.Column(db.String(20))

    date_of_birth = db.Column(db.Date)

    phone = db.Column(db.String(20))

    email = db.Column(db.String(120))

    address = db.Column(db.Text)

    joining_date = db.Column(db.Date)

    current_salary = db.Column(db.Float)

    profile_photo = db.Column(db.String(255))

    marital_status = db.Column(db.String(50))

    blood_group = db.Column(db.String(20))

    permanent_address = db.Column(db.Text)

    domicile_district = db.Column(db.String(100))

    alternate_phone = db.Column(db.String(20)) 




    status = db.Column(db.String(20), default="Active")
    department_id = db.Column(
        db.Integer,
    db.ForeignKey("departments.department_id")
 )

    designation_id = db.Column(
        db.Integer,
    db.ForeignKey("designations.designation_id")
 )

    supervisor_id = db.Column(db.Integer)

    created_at = db.Column(db.DateTime)

    department = db.relationship(
    "Department",
    backref="employees"
)

    designation = db.relationship(
    "Designation",
    backref="employees"
)
def __repr__(self):
        return f"<Employee {self.employee_name}>"