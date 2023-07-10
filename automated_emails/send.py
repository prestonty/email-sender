from email.message import EmailMessage  # this comes with python library
import ssl  # this adds a layer of security when sending emails
import smtplib

import os
from dotenv import load_dotenv

import csv

# read from env file
load_dotenv()
sender = os.getenv('sender')
password = os.getenv('pass')
# receiver = os.getenv('receiver')

# create the email body and message


# read from csv
with open('variables.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # skips the first row of the csv file (the header)
    for row in csv_reader:
        name = row[0]
        email = row[1]
        website = row[2]
        status = row[3]
        requested = row[4]
        received = row[5]
        money = row[6]

        # object used to write email
        em = EmailMessage()

        subject = 'BIG WIN'
        body = """congragulations, you won the lottery"""

        em['From'] = sender
        em['To'] = email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        # smtp.gmail.com is an email server used to send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, email, em.as_string())
