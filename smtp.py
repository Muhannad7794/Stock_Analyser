import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

# Email account credentials and settings from environment variables
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))  # Ensure port is an integer
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
receiver_email = "muhannadalulaby@gmail.com"

# SMTP server configuration and email content
subject = "Test Email from Python with dotenv"
body = """
Hi there,
This is a test email sent from a Python script using smtplib and dotenv for configuration.

Best,
Your Python Script
"""

# Setup email message
message = MIMEMultipart()
message["From"] = EMAIL_HOST_USER
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the SMTP server and send the email
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    if EMAIL_USE_TLS:
        server.starttls()  # Upgrade the connection to secure
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    text = message.as_string()
    server.sendmail(EMAIL_HOST_USER, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
