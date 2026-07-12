from flask_login import UserMixin
from extensions import db


class Supervisor(UserMixin, db.Model):

    __tablename__ = "supervisors"


    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)

    username = db.Column(db.String(50), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    email = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    status = db.Column(db.String(20), default="Active")

    #employees = db.relationship(
        #"Employee",
        #backref="supervisor",
        #lazy=True
    #)