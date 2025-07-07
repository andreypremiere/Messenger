import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# Здесь нужно оформить html красивую страницу и отправлять ее


def send_email(email: str, code: str | int) -> bool:
    """Отправка кода на email через SMTP с Яндекс Почты."""
    msg = EmailMessage()
    msg.set_content(f"Your verification code: {code}")
    msg["Subject"] = "Verification Code"
    msg["From"] = f"Messenger <{os.getenv('EMAIL_USER')}>"
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL("smtp.yandex.ru", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(msg)
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
