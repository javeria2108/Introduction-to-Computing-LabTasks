def get_contacts(my_contacts):
    names = []
    emails = []
    with open(my_contacts, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
from string import Template
def read_template(message):
    with open(message, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
import smtplib
s = smtplib.SMTP(host='smtp.gmail.com', port=465)
s.starttls()
s.login(i2cproject11@gmail.com, password789)
names, emails = get_contacts('mycontacts.txt')
message_template = read_template('message.txt')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
for name, email in zip(names, emails):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name.title(jav))
    msg['From']=i2cproject11@gmail.com
    msg['To']=jaizeejane@gmail.com
    msg['Subject']="This is TEST"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
