# import os
# import base64
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request

# def send_email(sender, to, subject, message):

#     # declare scope
#     scopes = ['https://www.googleapis.com/auth/gmail.send']

#     # Load credentials from the JSON file downloaded from GCP
#     credentials = Credentials.from_authorized_user_file('automated_emails/credentials.json', scopes)

#     # If the credentials are expired, refresh them
#     if credentials.expired and credentials.refresh_token:
#         credentials.refresh(Request())

#     # Create the Gmail API client
#     service = build('gmail', 'v1', credentials=credentials)

#     # Create an email message
#     message = create_message(sender, to, subject, message)

#     # Send the email
#     send_message(service, 'me', message)

# def create_message(sender, to, subject, message_text):
#     message = {
#         'from': sender,
#         'to': to,
#         'subject': subject,
#         'text': message_text
#     }
#     encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
#     return {'raw': encoded_message}

# def send_message(service, user_id, message):
#     try:
#         service.users().messages().send(userId=user_id, body=message).execute()
#         print("Email sent successfully!")
#     except Exception as e:
#         print("An error occurred while sending the email:", str(e))

# # Example usage
# sender = 'preston.tomying@gmail.com'
# to = 'kyle.tomying@example.com'
# subject = 'Hello from Python!'
# message = 'This is the content of the email.'

# send_email(sender, to, subject, message)
