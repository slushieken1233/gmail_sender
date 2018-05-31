# first we import libraries
import smtplib
import getpass

# python 2/3 compatibility: https://stackoverflow.com/a/21731110
try:
	input = raw_input
except NameError:
	pass

# get gmail info from console
username = input("Enter your gmail account: ")
password = getpass.getpass("Enter your gmail password: ")
to = input("Enter the reciepient : ")
message = input("Enter your message: ")

# set our variables/account info
sender_email_id = username
sender_password = password
recipient_email_id = to

# next we create the session with definitions
session = smtplib.SMTP('smtp.gmail.com', 587)

# wrap it in TLS
session.starttls()

# Authentication
session.login(sender_email_id, sender_password)

# Send it!
session.sendmail(sender_email_id, recipient_email_id, message)

# Quit
session.quit

