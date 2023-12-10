def get_contacts(contacts):
    names = []
    emails = []
    with open("contacts.txt",'r') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
names, emails = get_contacts('contacts.txt')
import itertools
for (x,y) in zip(names,emails):
    import os
    import smtplib
    EMAIL_ADDRESS= 'i2cproject11@gmail.com'
    PASSWORD= 'Password789'
    reciever=y
    with smtplib.SMTP('smtp.gmail.com', 587)as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, PASSWORD)
        subject= 'REAL TIME'
        body='Dear',x,'Are you working on it?'
        msg= f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS,reciever,msg)

print('status:email delivered')
print('Sent history:')
import imaplib                              
import email
from email.header import decode_header
import webbrowser
import os
server ="imap.gmail.com"                     
imap = imaplib.IMAP4_SSL(server)
username ="i2cproject11@gmail.com" 
password ="Password789"
imap.login(username, password)
res, messages = imap.select('"[Gmail]/Sent Mail"')
messages = int(messages[0])
n=10
for i in range(messages, messages - n, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")     
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            From = msg["From"]
            To=emails
            subject = msg["Subject"]
            print("From : ", From)
            print("To:",To)
            print("subject : ", subject)
  
