# seed_users.py

from app import create_app
from app.models import get_db

# Create the Flask app
app = create_app()

# Insert test users
with app.app_context():
    db = get_db()

    users = [
        ("Emma Johnson", "emma.johnson@example.com"),
        ("Liam Brown", "liam.brown@example.com"),
        ("Olivia Davis", "olivia.davis@example.com"),
        ("Noah Wilson", "noah.wilson@example.com"),
        ("Ava Thompson", "ava.thompson@example.com")
    ]

    for name, email in users:
        db.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))

    db.commit()
    print("✅ 5 test users inserted into campaigns.db")
