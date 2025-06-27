# send_test.py

from app import create_app
from app.utils import send_phishing_email

app = create_app()

with app.app_context():
    send_phishing_email("samowner706341@gmail.com", "Sayan Mandal")
