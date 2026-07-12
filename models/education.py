from extensions import db


class Education(db.Model):
    __tablename__ = "employee_education"

    education_id = db.Column(
        db.Integer,
        primary_key=True
    )

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.employee_id"),
        nullable=False
    )

    degree = db.Column(
        db.String(100)
    )

    institute_name = db.Column(
        db.String(200)
    )

    board_university = db.Column(
        db.String(200)
    )

    passing_year = db.Column(
        db.Integer
    )

    percentage_cgpa = db.Column(
        db.String(20)
    )

    education_status = db.Column(
        db.String(50)
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )

    employee = db.relationship(
        "Employee",
        backref="educations"
    )

    def __repr__(self):
        return f"<Education {self.degree}>"