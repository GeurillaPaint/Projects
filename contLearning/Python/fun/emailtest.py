import smtplib

gmail_user = raw_input('Enter Email: ')
gmail_name = raw_input('Enter new username: ')
gmail_password = raw_input('Enter Password: ')#removed password for security reasons lol

sent_from = gmail_user
to = ['phill@elacarte.com']
subject = 'Test'
body = 'Hello, \n\n Your Username is: ' + gmail_name + '\nYour password is: ' + gmail_password + '\n\nRegards,\n\n Account Management'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:
    print 'Something went wrong...'
