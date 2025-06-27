from flask import Blueprint, render_template, request, redirect, url_for
from app.utils import send_phishing_email
from app.models import get_db
import datetime

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/send', methods=['POST'])
def send():
    db = get_db()
    users = db.execute('SELECT * FROM users').fetchall()
    for user in users:
        send_phishing_email(user['email'], user['name'])
        db.execute('INSERT INTO emails (user_id, sent_at) VALUES (?, ?)', (user['id'], datetime.datetime.now()))
    db.commit()
    return redirect(url_for('routes.dashboard'))

@bp.route('/dashboard')
def dashboard():
    db = get_db()
    stats = db.execute('''SELECT COUNT(*) as total, 
                                 SUM(clicked_at IS NOT NULL) as clicked, 
                                 SUM(submitted_at IS NOT NULL) as submitted 
                          FROM emails''').fetchone()
    return render_template('dashboard.html', stats=stats)
