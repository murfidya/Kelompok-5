from flask import Flask, redirect, url_for
from extensions import db, bcrypt, login_manager, migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '8f42a73c2c3f4b32a1ec54f7c2ef9c8d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_organizer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

from blueprints.auth import auth_bp
from blueprints.dashboard import dashboard_bp
from blueprints.tasks import tasks_bp
from blueprints.assignments import assignments_bp
from blueprints.exams import exams_bp
from blueprints.notes import notes_bp
from blueprints.calendar import calendar_bp

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(tasks_bp)
app.register_blueprint(assignments_bp)
app.register_blueprint(exams_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(calendar_bp)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
