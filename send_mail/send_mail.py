# Envia email pelo servidor de email usando o protocolo smtp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'dev.testm4il@gmail.com'
password = 'test@1234'

def send_mail(text='Email Body', subject='Hello World',
              from_email='Test Mail <dev.testm4il@gmail.com>', to_emails=[],
              html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)


    server.quit()


