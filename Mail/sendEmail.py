# coding=utf8

'''
version: October 04, 2019 04:39 PM
Last revision: October 04, 2019 04:51 PM
  
Author : Chao-Hsuan Ke

'''

'''
Reference

https://blog.taiker.space/python-how-to-send-an-email-with-python/

Google setting
https://www.lightblue.asia/send-gmail-by-python/
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = ""   # your gmail account
to_email = ""       # who receive this mail 
password = ""       # your gmail password
Subject = ""        # mail subject
body = ""           # your mail message

#context
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = to_email
msg['Subject'] = Subject


msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
text = msg.as_string()
server.sendmail(msg['From'], msg['To'], text)
server.quit()
