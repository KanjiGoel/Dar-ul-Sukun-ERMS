from extensions import db

class Designation(db.Model):

    __tablename__ = "designations"

    designation_id = db.Column(
        db.Integer,
        primary_key=True
    )

    designation_name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    

    description = db.Column(
        db.Text
    )

    basic_salary = db.Column(
        db.Float,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<designation {self.designation_name}>"