from email.message import EmailMessage  # this comes with python library
import ssl  # this adds a layer of security when sending emails
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv('sender')
password = os.getenv('pass')
receiver = os.getenv('receiver')

subject = 'BIG WIN'
body = """congragulations, you won the lottery"""

# object used to write email
em = EmailMessage()

em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# smtp.gmail.com is an email server used to send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())
