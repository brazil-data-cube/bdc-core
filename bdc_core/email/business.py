import smtplib
import logging
from email.headerregistry import Address
from email.message import EmailMessage
from mako.template import Template

from .config import SMTP_PORT, SMTP_HOST, EMAIL_ADDRESS, EMAIL_PASSWORD, BASE_PATH_TEMPLATES

class EmailBusiness(object):

    def __init__(self, username, email_addr, subject, template, body_args=None):
        self.to = self.mount_user(username, email_addr)
        self.email_msg = self.mount_email(template, subject, body_args)
    
    def mount_user(self, name, email_addr) -> Address:
        return Address(display_name=name, addr_spec=email_addr)

    def mount_email(self, template, subject, args) -> EmailMessage:
        template = Template(filename='{}/{}.txt'.format(BASE_PATH_TEMPLATES, template))
        text = template.render(args=args)

        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.to
        msg['Subject'] = subject
        msg.set_content(text)
        return msg
        
    def send(self):
        try:
            with smtplib.SMTP(SMTP_HOST, port=SMTP_PORT) as smtp_server:
                smtp_server.ehlo()
                smtp_server.starttls()
                smtp_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp_server.send_message(self.email_msg)
            return True
        except Exception as e:
            logging.error(str(e))
            return False