from os import environ
from email.message import EmailMessage
import ssl
import smtplib

def send_verification_email(email, link):
    """Sends a verifiation email to the provided email address."""

    sender = environ.get("EMAIL_ACCOUNT")

    em = EmailMessage()
    em["From"] = sender
    em["To"] = email
    em["Subject"] = "Verify your e-mail"
    em.set_content(
       f"""
        Thanks for you interest in recipeats! Please click the link below to verify your e-mail address:

        {link}
        """
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, environ.get("EMAIL_PASSWORD"))
        smtp.sendmail(sender, email, em.as_string())