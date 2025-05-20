from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models import Task, Assignment, Exam
from datetime import datetime, timedelta, timezone
import calendar

calendar_bp = Blueprint('calendar', __name__)

def get_month_calendar(year, month):
    # Get the calendar for the specified month
    cal = calendar.monthcalendar(year, month)
    
    # Get the first and last day of the month with timezone awareness
    first_day = datetime(year, month, 1, tzinfo=timezone.utc)
    if month == 12:
        last_day = datetime(year + 1, 1, 1, tzinfo=timezone.utc) - timedelta(days=1)
    else:
        last_day = datetime(year, month + 1, 1, tzinfo=timezone.utc) - timedelta(days=1)

    # Get all events for the current month
    tasks = Task.query.filter_by(user_id=current_user.id)\
        .filter(Task.due_date >= first_day)\
        .filter(Task.due_date <= last_day)\
        .all()
    
    assignments = Assignment.query.filter_by(user_id=current_user.id)\
        .filter(Assignment.due_date >= first_day)\
        .filter(Assignment.due_date <= last_day)\
        .all()
    
    exams = Exam.query.filter_by(user_id=current_user.id)\
        .filter(Exam.exam_date >= first_day)\
        .filter(Exam.exam_date <= last_day)\
        .all()

    # Create events dictionary
    events = {}
    for task in tasks:
        day = task.due_date.day
        if day not in events:
            events[day] = {'tasks': [], 'assignments': [], 'exams': []}
        events[day]['tasks'].append(task)

    for assignment in assignments:
        day = assignment.due_date.day
        if day not in events:
            events[day] = {'tasks': [], 'assignments': [], 'exams': []}
        events[day]['assignments'].append(assignment)

    for exam in exams:
        day = exam.exam_date.day
        if day not in events:
            events[day] = {'tasks': [], 'assignments': [], 'exams': []}
        events[day]['exams'].append(exam)

    return cal, events

@calendar_bp.route('/calendar')
@login_required
def calendar_view():
    # Get current year and month with timezone awareness
    today = datetime.now(timezone.utc)
    year = today.year
    month = today.month
    
    # Get calendar and events
    cal, events = get_month_calendar(year, month)
    
    # Get month name
    month_name = calendar.month_name[month]
    
    return render_template('calendar.html',
                         calendar=cal,
                         events=events,
                         month_name=month_name,
                         year=year,
                         month=month,
                         today=today.day,
                         now=today)

@calendar_bp.route('/calendar/<int:year>/<int:month>')
@login_required
def calendar_month(year, month):
    # Validate month
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1
    
    # Get calendar and events
    cal, events = get_month_calendar(year, month)
    
    # Get month name
    month_name = calendar.month_name[month]
    
    # Get today's day if current month with timezone awareness
    today = datetime.now(timezone.utc)
    today_day = today.day if today.year == year and today.month == month else None
    
    return render_template('calendar.html',
                         calendar=cal,
                         events=events,
                         month_name=month_name,
                         year=year,
                         month=month,
                         today=today_day,
                         now=today)
