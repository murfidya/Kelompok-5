from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Assignment
from extensions import db
from datetime import datetime, timezone

assignments_bp = Blueprint('assignments', __name__)

@assignments_bp.route('/assignments')
@login_required
def assignments():
    user_assignments = Assignment.query.filter_by(user_id=current_user.id).order_by(Assignment.due_date).all()
    return render_template('assignments.html', assignments=user_assignments)

@assignments_bp.route('/assignments/add', methods=['GET', 'POST'])
@login_required
def add_assignment():
    if request.method == 'POST':
        subject = request.form.get('subject')
        title = request.form.get('title')
        due_date_str = request.form.get('due_date')
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('assignments.add_assignment'))

        new_assignment = Assignment(
            subject=subject,
            title=title,
            due_date=due_date,
            user_id=current_user.id
        )
        db.session.add(new_assignment)
        db.session.commit()
        flash('Assignment added successfully!', 'success')
        return redirect(url_for('assignments.assignments'))
    return render_template('add_assignment.html')

@assignments_bp.route('/assignments/edit/<int:assignment_id>', methods=['GET', 'POST'])
@login_required
def edit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if assignment.user_id != current_user.id:
        flash('You do not have permission to edit this assignment.', 'danger')
        return redirect(url_for('assignments.assignments'))

    if request.method == 'POST':
        assignment.subject = request.form.get('subject')
        assignment.title = request.form.get('title')
        due_date_str = request.form.get('due_date')
        try:
            assignment.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('assignments.edit_assignment', assignment_id=assignment_id))
        
        assignment.completed = 'completed' in request.form
        db.session.commit()
        flash('Assignment updated successfully!', 'success')
        return redirect(url_for('assignments.assignments'))
    return render_template('edit_assignment.html', assignment=assignment)

@assignments_bp.route('/assignments/delete/<int:assignment_id>', methods=['POST'])
@login_required
def delete_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if assignment.user_id != current_user.id:
        flash('You do not have permission to delete this assignment.', 'danger')
        return redirect(url_for('assignments.assignments'))
    
    db.session.delete(assignment)
    db.session.commit()
    flash('Assignment deleted successfully!', 'success')
    return redirect(url_for('assignments.assignments'))
