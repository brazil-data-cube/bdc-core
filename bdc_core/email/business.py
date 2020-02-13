#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This file contains the common utilities send email Brazil Data Cube projects."""

import logging
import smtplib
from email.headerregistry import Address
from email.message import EmailMessage
from mako.template import Template

from .config import SMTP_PORT, SMTP_HOST, EMAIL_ADDRESS, \
    EMAIL_PASSWORD, BASE_PATH_TEMPLATES

class EmailBusiness:
    """Class to send emails."""

    def __init__(self, username, email_addr, subject, template, **kwargs):
        """Builds Email factory.

        Args:
            username (string) - Full Name Recipient.
            email_addr (string) - Email Recipient.
            subject (string) - subject email.
            template (string) - template title.
            args (dict) - args to mount template
        """
        self.to = self.mount_user(username, email_addr)
        self.email_msg = self.mount_email(
            template,
            subject,
            kwargs.get('body_args')
        )


    def mount_user(self, name, email_addr) -> Address:
        """Mount user recipient object."""
        return Address(display_name=name, addr_spec=email_addr)

    def mount_email(self, template, subject, args) -> EmailMessage:
        """Mount email recipient object."""
        template = Template(filename='{}/{}.txt'.format(
            BASE_PATH_TEMPLATES, template))
        text = template.render(args=args)

        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.to
        msg['Subject'] = subject
        msg.set_content(text)
        return msg

    def send(self):
        """Dispatch email."""
        try:
            with smtplib.SMTP(SMTP_HOST, port=int(SMTP_PORT)) as smtp_server:
                smtp_server.ehlo()
                smtp_server.starttls()
                smtp_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp_server.send_message(self.email_msg)
            return True
        except smtplib.SMTPException as e:
            logging.error(str(e))
            return False
