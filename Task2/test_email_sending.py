import os 
import smtplib 
from email.message import EmailMessage
import ssl
import random

os.environ['EMAIL_PASS'] = 'omsm cmtw vxem vlju'

EMAIL_ADDRESS = 'husseinemad064@gmail.com'
email_receiver = 'husseinemad064@gmail.com'
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# print(os.environ)
print(EMAIL_ADDRESS)
# create 6-digit number 
num = random.randint(100000,999999)


body=f"""
 Your OTP Verification Code is {num}
"""
em = EmailMessage()
em['From'] = EMAIL_ADDRESS
em['To'] = email_receiver
em['Subject'] = f'OTP Verification Code Delivered '
em.set_content(body)

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(em)
