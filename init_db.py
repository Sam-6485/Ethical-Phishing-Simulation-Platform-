# init_db.py
from app import create_app
from app.models import init_db

app = create_app()

with app.app_context():
    init_db()
    print("Database campaigns.db initialized.")
