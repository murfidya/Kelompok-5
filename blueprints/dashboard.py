from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Task, Assignment, Exam
from datetime import datetime, timezone

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # Get current time in UTC
    now = datetime.now(timezone.utc)

    # Fetch upcoming tasks, assignments, and exams for the current user
    tasks = Task.query.filter_by(user_id=current_user.id, completed=False)\
        .filter(Task.due_date >= now)\
        .order_by(Task.due_date).all()
    assignments = Assignment.query.filter_by(user_id=current_user.id, completed=False)\
        .filter(Assignment.due_date >= now)\
        .order_by(Assignment.due_date).all()
    exams = Exam.query.filter_by(user_id=current_user.id)\
        .filter(Exam.exam_date >= now)\
        .order_by(Exam.exam_date).all()

    return render_template('dashboard.html', tasks=tasks, assignments=assignments, exams=exams)
