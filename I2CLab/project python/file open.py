f=open("emails.txt")
import os
import smtplib

EMAIL_ADDRESS= 'i2cproject11@gmail.com'
PASSWORD= 'Password789'
for x in f:
    reciever= x
    with smtplib.SMTP('smtp.gmail.com', 587)as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, PASSWORD)
        subject= 'Project'
        body='''Dear Are you working on it?'''
        msg= f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS,reciever,msg)
