#!/usr/bin/python2.7
import smtplib
import time
import imaplib
import email
import imaplib
import base64
import os
import email
#My Personal Assistant
#Possible Features to adds
#Check emails
#Reply emails
#Send emails
#Check news
#Post to Facebook / twitter / telegram / WhatsApp
#Read SMS
#Download YouTube videos
#Summarise articles
#Read articles
#Set reminders / schedule tasks
#Check past events
#Google search
#Download files
#Recommend movies, songs or articles
#Send bulk SMS
def CheckNewEmails():
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com','993')
        mail.login('jamiecmacleod@gmail.com','tdxqiydpihfmoekzb')
        mail.select('inbox')
        type, data = mail.search(None, 'UNSEEN')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'
                    print(msg.get_payload(decode=True))

    except Exception, e:
        print str(e)
CheckNewEmails()
