import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from openai import OpenAI

# Load credentials from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "support@ero.solar"
SENDER_PASSWORD = os.environ.get("SMTP_PASSWORD")
RECIPIENT_EMAIL = "support@openai.com"

# All models to test
models = [
    'gpt-5.2',
    'gpt-5.2-2025-12-11',
    'gpt-5.2-chat-latest',
    'gpt-5.2-pro',
    'gpt-5.2-pro-2025-12-11',
]

for model in models:
    print(f"Testing {model}...")

    try:
        response = client.responses.create(
            model=model,
            input=f"Write a brief friendly hello for an email. Sign off as {model}."
        )
        greeting = response.output_text
        status = "✓ AVAILABLE"
    except Exception as e:
        if "does not exist" in str(e):
            status = "✗ NOT AVAILABLE"
            greeting = f"This model ({model}) is not available."
        else:
            status = "✗ ERROR"
            greeting = f"Error testing {model}: {str(e)[:100]}"

    body = f"{greeting}\n\nModel: {model}\nStatus: {status}\n\nThis email was sent from {model} on a verified API account."

    # Create email
    msg = MIMEMultipart()
    msg["From"] = f"{model} on a verified API account <{SENDER_EMAIL}>"
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = f"Hello from {model} - {status}"
    msg.attach(MIMEText(body, "plain"))

    # Send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print(f"{model}: {status} - Email sent")
    except Exception as e:
        print(f"{model}: {status} - SMTP Error: {e}")
