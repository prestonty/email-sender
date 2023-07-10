How to use (As of 4:27 pm July 10, 2023):

The sender email should have two step verification on. Navigate to "Manage Google Account" and under "Security", turn on 2-Step-Verification.

After 2-Step is turned on, type in the following link into your search bar: [https://myaccount.google.com/u/4/apppasswords](url)
In the prompt "Select App" choose "Other (Custom name)" and give it any custom name.
Copy the 16 character password.

Create a .env file in the automated_emails folder
Inside the file, it should look something like this:
sender=senderEmail@gmail.com
pass=your_16_character_password
receiver=receiverEmail@gmail.com
