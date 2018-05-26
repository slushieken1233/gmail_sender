import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##
#   pysendmail-parc.py - Send an email from PARC's exchange servers from the CLI
#    - Sebastian Safari (c) 2018
##

help_text = 'Sample usage: python pysendmail-parc.py <to>@parc.com <from>@parc.xerox.com "Subject" "Body etc"'

if len(sys.argv) < 2:
    print("You need arguments!")
    print(help_text)    
    exit(1)
elif len(sys.argv) < 5 and "h" in sys.argv:
    print(help_text)    
    exit(1)
elif len(sys.argv) < 5 :
    print(help_text)    
    exit(1)
else:
    em_to = sys.argv[1]
    em_from = sys.argv[2]
    em_subject = sys.argv[3]
    em_body = sys.argv[4]
    print("Emailing: " + em_to)

    msg = MIMEMultipart()    
    
    address_book = [em_to]
    msg['From'] = em_from
    msg['To'] = ','.join(address_book)
    msg['Subject'] = em_subject
    msg.attach(MIMEText(em_body, 'plain'))
    text=msg.as_string()
    
    # Send the message via our SMTP server
    s = smtplib.SMTP('exchangehub.ad.parc.com')
    s.sendmail(em_from,address_book, text)
    s.quit()        

