import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, From, Content

# def send_email(email: str, content: str, subject: str = "No subject"):
#     api_key = os.environ.get("SENDGRID_API_KEY")

#     sendgrid_client = SendGridAPIClient(api_key)

#     message = Mail(
#         from_email=From(email="testeps2fase@gmail.com", name="FinTrack"),
#         to_emails=[To(email=email)],
#         subject=subject,
#         html_content=content  
#     )

#     sendgrid_client.send(message)

import smtplib  
from email.mime.text import MIMEText  

sender = "testeps2fase@gmail.com" 
password = os.environ.get("GMAIL_PASSWORD")

def send_email(email, conteudo):
    msg = MIMEText(conteudo)
    msg['Subject'] = "FinTrack - Redefinição de senha"  
    msg['From'] = sender  
    msg['To'] = email  
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password) 
        smtp_server.sendmail(sender, email, msg.as_string())  
    