from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Note
from extensions import db
from datetime import datetime

notes_bp = Blueprint('notes', __name__, template_folder='templates')

@notes_bp.route('/notes')
@login_required
def notes():
    user_notes = Note.query.filter_by(user_id=current_user.id).order_by(Note.date_created.desc()).all()
    return render_template('notes.html', notes=user_notes)

@notes_bp.route('/notes/add', methods=['GET', 'POST'])
@login_required
def add_note():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        subject = request.form.get('subject')

        if not title or not subject:
            flash('Title and subject are required.', 'danger')
            return redirect(url_for('notes.add_note'))

        new_note = Note(
            title=title,
            content=content,
            subject=subject,
            user_id=current_user.id,
            date_created=datetime.utcnow()
        )
        db.session.add(new_note)
        db.session.commit()
        flash('Note added successfully!', 'success')
        return redirect(url_for('notes.notes'))
    return render_template('add_note.html')

@notes_bp.route('/notes/edit/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash('You do not have permission to edit this note.', 'danger')
        return redirect(url_for('notes.notes'))

    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        note.subject = request.form.get('subject')

        if not note.title or not note.subject:
            flash('Title and subject are required.', 'danger')
            return redirect(url_for('notes.edit_note', note_id=note_id))

        db.session.commit()
        flash('Note updated successfully!', 'success')
        return redirect(url_for('notes.notes'))
    return render_template('edit_note.html', note=note)

@notes_bp.route('/notes/delete/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash('You do not have permission to delete this note.', 'danger')
        return redirect(url_for('notes.notes'))
    
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully!', 'success')
    return redirect(url_for('notes.notes'))

@notes_bp.route('/notes/view/<int:note_id>')
@login_required
def view_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash('You do not have permission to view this note.', 'danger')
        return redirect(url_for('notes.notes'))
    return render_template('view_note.html', note=note)
