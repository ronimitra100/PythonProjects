import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Roni From'
email['to'] = 'ronidevemail@gmail.com'
email['subject'] = 'You won a million dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ronidevemail@gmail.com', 'mypassword!')
    smtp.send_message(email)
    print('all good boss!')