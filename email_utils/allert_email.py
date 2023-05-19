import yagmail
from email_configs import *
'''Note, email configs holds the "user", "reciever" and "app_password" '''

body = "Hello there from Yagmail"

def send_email(subject, text, reciever = receiver):
    yag = yagmail.SMTP(user = user, password=app_password)
    yag.send(
        to=receiver,
        subject=subject,
        contents=text, 
        attachments=None,
    )

# print(os.path.exists('/proc/560250'))

# filename = "document.pdf"
if __name__ == "__main__":
    print("sending test email to {}".format(receiver))
    send_email("test email", "test email body.")