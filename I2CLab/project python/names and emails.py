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
        subject= 'Project'
        body='Dear',x,'Are you working on it?'
        msg= f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS,reciever,msg)

