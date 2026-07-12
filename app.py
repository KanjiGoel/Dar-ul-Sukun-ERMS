


from flask import Flask, render_template
from config import Config
from extensions import db
from models.supervisor import Supervisor
from models.designation import Designation
from models.employee import Employee
from routes.designation import designation
from routes.employee import employee
from models.education import Education
from models.document import Document
from routes.dashboard import dashboard





# Blueprint import
from routes.auth import auth
from routes.auth import auth
from routes.employee import employee
from routes.designation import designation
from routes.education import education
from routes.document import document


app = Flask(__name__)

app.config.from_object(Config)
app.config["SECRET_KEY"] = "dar_ul_sukun_secret_key"




db.init_app(app)

# Register Blueprint
app.register_blueprint(auth)
app.register_blueprint(designation)
app.register_blueprint(employee)
app.register_blueprint(education)
app.register_blueprint(document)
app.register_blueprint(dashboard)


@app.route("/")
def home():
    return render_template("index.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)