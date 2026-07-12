from extensions import db


class Document(db.Model):
    __tablename__ = "employee_documents"

    document_id = db.Column(
        db.Integer,
        primary_key=True
    )

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.employee_id"),
        nullable=False
    )

    document_type = db.Column(
        db.String(100),
        nullable=False
    )

    file_path = db.Column(
        db.String(255)
    )

    upload_date = db.Column(
        db.DateTime,
        default=db.func.now()
    )

    notes = db.Column(
        db.Text
    )

    employee = db.relationship(
        "Employee",
        backref="documents"
    )

    def __repr__(self):
        return f"<Document {self.document_type}>"