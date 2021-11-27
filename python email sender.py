#!/usr/bin/python
#This will send a email. 
#pip install sendmail
import smtplib, string
import os, time
#not sure this was from the book does not matter if comment in or out will still send message.
#os.system("/etc/init.d/sendmail start")
time.sleep(4)


SUBJECT = "Hey Prof I got a file for you to look at"
#add email you want to use here. I coul make it an input but i am lazy
TO = "gj2976020@gmail.com"
#The email and password used to send the email.
FROM = "gsaabstudent@gmail.com"
EMAIL_PASSWORD = "$tudent#2021"
TEXT = "Hello Sir or Madam you have just won a brand new car"
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    TEXT
    ),)
server = smtplib.SMTP(host="smtp.gmail.com", port=587)
# connect to the SMTP server as TLS mode ( for security )
server.starttls()
# login to the email account
server.login(FROM, EMAIL_PASSWORD)
server.sendmail(FROM, [TO], BODY)
server.quit()

time.sleep(4)
#os.system("/etc/init.d/sendmail stop")