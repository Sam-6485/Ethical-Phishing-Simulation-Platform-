from flask import Blueprint, request, redirect, render_template
from app.models import get_db
import datetime

bp = Blueprint('tracking', __name__)

@bp.route('/track/<int:email_id>')
def track(email_id):
    db = get_db()
    db.execute('UPDATE emails SET clicked_at = ? WHERE id = ?', (datetime.datetime.now(), email_id))
    db.commit()
    return render_template('email_template.html', email_id=email_id)

@bp.route('/submit/<int:email_id>', methods=['POST'])
def submit(email_id):
    db = get_db()
    db.execute('UPDATE emails SET submitted_at = ? WHERE id = ?', (datetime.datetime.now(), email_id))
    db.commit()
    return redirect('/education')

@bp.route('/education')
def education():
    return render_template('education.html')
