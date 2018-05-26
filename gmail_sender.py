# first we import libraries
import smtplib

# set our variables/account info
sender_email_id = "<Gmail username>"
sender_password = "<Gmail Password>"
message = "<Email Message>"
recipient_email_id = "<Recipient Email Address>"

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

