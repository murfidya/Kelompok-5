from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Task
from extensions import db
from datetime import datetime, timezone

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks')
@login_required
def tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date).all()
    return render_template('tasks.html', tasks=user_tasks)

@tasks_bp.route('/tasks/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        due_date_str = request.form.get('due_date')
        try:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('tasks.add_task'))

        new_task = Task(title=title, description=description, due_date=due_date, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('tasks.tasks'))
    return render_template('add_task.html')

@tasks_bp.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('You do not have permission to edit this task.', 'danger')
        return redirect(url_for('tasks.tasks'))

    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        due_date_str = request.form.get('due_date')
        try:
            task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'danger')
            return redirect(url_for('tasks.edit_task', task_id=task_id))
        task.completed = 'completed' in request.form
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.tasks'))
    return render_template('edit_task.html', task=task)

@tasks_bp.route('/tasks/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('You do not have permission to delete this task.', 'danger')
        return redirect(url_for('tasks.tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks.tasks'))
