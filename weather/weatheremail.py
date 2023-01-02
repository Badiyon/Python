import smtplib
import ssl

#email, smtp server, and passwords have been left blank since I do not want to
#publish some of this information on GitHub
def sendMail():
    port = 465
    smtp_server = ""
    sender_email = ""
    receiver_email = ""
    password = ""
    message = """\
    Subject: Weather Alert
    
    Be aware of weather problems in """

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)