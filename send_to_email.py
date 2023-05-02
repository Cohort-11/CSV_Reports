from email.message import EmailMessage
import os
import ssl
import smtplib
"""This module sends an email with the report"""

# Add your email here
email_sender = ""

email_password = os.environ.get("EMAIL_PASSWORD")
# Email of the person you're sending the report to
email_receiver = ""

with open('active.txt', 'r') as fp:
    content = fp.read()

subject = "Data for Cohort 11 Students"
body = content

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())