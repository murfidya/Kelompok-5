from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Exam
from extensions import db
from datetime import datetime, timezone

exams_bp = Blueprint('exams', __name__, template_folder='templates')

@exams_bp.route('/exams')
@login_required
def exams():
    now = datetime.now(timezone.utc)
    user_exams = Exam.query.filter_by(user_id=current_user.id).order_by(Exam.exam_date).all()
    # Ensure all exam dates are timezone-aware
    for exam in user_exams:
        if exam.exam_date.tzinfo is None:
            exam.exam_date = exam.exam_date.replace(tzinfo=timezone.utc)
    return render_template('exams.html', exams=user_exams, now=now)

@exams_bp.route('/exams/add', methods=['GET', 'POST'])
@login_required
def add_exam():
    if request.method == 'POST':
        subject = request.form.get('subject')
        exam_date_str = request.form.get('exam_date')
        try:
            exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('exams.add_exam'))

        new_exam = Exam(
            subject=subject,
            exam_date=exam_date,
            user_id=current_user.id
        )
        db.session.add(new_exam)
        db.session.commit()
        flash('Exam added successfully!', 'success')
        return redirect(url_for('exams.exams'))
    return render_template('add_exam.html')

@exams_bp.route('/exams/edit/<int:exam_id>', methods=['GET', 'POST'])
@login_required
def edit_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    if exam.user_id != current_user.id:
        flash('You do not have permission to edit this exam.', 'danger')
        return redirect(url_for('exams.exams'))

    if request.method == 'POST':
        exam.subject = request.form.get('subject')
        exam_date_str = request.form.get('exam_date')
        try:
            exam.exam_date = datetime.strptime(exam_date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('exams.edit_exam', exam_id=exam_id))

        db.session.commit()
        flash('Exam updated successfully!', 'success')
        return redirect(url_for('exams.exams'))
    return render_template('edit_exam.html', exam=exam)

@exams_bp.route('/exams/delete/<int:exam_id>', methods=['POST'])
@login_required
def delete_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    if exam.user_id != current_user.id:
        flash('You do not have permission to delete this exam.', 'danger')
        return redirect(url_for('exams.exams'))
    
    db.session.delete(exam)
    db.session.commit()
    flash('Exam deleted successfully!', 'success')
    return redirect(url_for('exams.exams'))
