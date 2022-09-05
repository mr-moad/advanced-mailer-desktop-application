import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr


def mail_sender(data):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = formataddr((data['from_name'], data['from_email']))
        msg['To'] = data['to_email']
        msg['Subject'] = data["subject"]
        if data.get('html_message'):
            html = data['html_message']
            msg.attach(MIMEText(html, 'html'))
        else:
            text = data.get('text_message')
            msg.attach(MIMEText(text, 'text'))
        s = None

        if data['smtp_encryption']:
            s = smtplib.SMTP_SSL(data['smtp_server'], data['smtp_port'])
        else:
            s = smtplib.SMTP(data['smtp_server'], data['smtp_port'])
        s.ehlo()
        s.starttls()
        s.login(user=data["smtp_email"], password=data["smtp_password"])
        s.sendmail(data['from_email'], data['to_email'], msg.as_string())
        s.quit()
        print(data['to_email'], "sent!")
    except:
        exit("email not sent")


# from email.header import Header
#
# def mail_sender(data):
#     msg = MIMEMultipart('alternative')
#     msg['From'] = formataddr((data['from_name'], data['from_email']))
#     msg['To'] = data['to_email']
#     msg['Subject'] = data["subject"]
#     if data.get('html_message'):
#         html = data['html_message']
#         msg.attach(MIMEText(html, 'html'))
#     else:
#         text = data.get('text_message')
#         msg.attach(MIMEText(text, 'text'))
#     s = None
#     # if data['smtp_encryption']:
#     #     s = smtplib.SMTP_SSL(data['smtp_server'], data['smtp_port'])
#     # else:
#
#     s = smtplib.SMTP(data['smtp_server'], str(data['smtp_port']))
#     s.ehlo()
#     s.starttls()
#     s.login(user=data["smtp_email"], password=data["smtp_password"])
#     s.sendmail(data['from_email'], data['to_email'], msg.as_string())
#     s.quit()
#     print(data['to_email'], "sent!")