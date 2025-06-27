import smtplib
from email.mime.text import MIMEText
from flask import current_app

def send_phishing_email(recipient, name):
    link = f"http://localhost:5000/track/1"  # In production, use real email_id
    html = f"""
    <html><body>
    <p>Hello {name},</p>
    <p>Urgent: Please <a href='{link}'>log in</a> to verify your account.</p>
    </body></html>
    """
    msg = MIMEText(html, 'html')
    msg['Subject'] = 'Account Verification Required'
    msg['From'] = current_app.config['SENDER_EMAIL']
    msg['To'] = recipient

    with smtplib.SMTP(current_app.config['SMTP_SERVER'], current_app.config['SMTP_PORT']) as server:
        server.send_message(msg)
def send_phishing_email(to_email, name):
    print(f"[SIMULATED EMAIL] Sent to {to_email} (Name: {name})")
