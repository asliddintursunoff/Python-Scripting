import smtplib
from email.message import EmailMessage
import random
def email_sender(reciever , msg_subject ):
    msg = random.randint(1000,10000)
    from_email = "asliddintursunoff25@gmail.com"
    sms = EmailMessage()
    sms['From'] = "Breaking9"
    sms['To'] = reciever
    sms['Subject'] = msg_subject
    sms.set_content(str(msg))
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login( from_email, "wpag dbxk wyzr vjrt")
    server.send_message(sms)
    return int(msg)
print("what's Up my friend👌\nPlease sign in")
your_email = input("Enter your email: ")
code = email_sender(your_email ,"Authentication code" )
print(print("We sent code to your email, Check it \n"))

while True:
    your_password = int(input("Enter Code: "))
    if your_password == code:
        print("Succesfully done!")
        break
    else:
        print("Wrong code!!!\nPlease enter again: ")


