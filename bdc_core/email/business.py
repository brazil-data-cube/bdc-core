#
# This file is part of BDC Core.
# Copyright (C) 2019-2020 INPE.
#
# BDC Core is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""This file contains the common utilities send email Brazil Data Cube projects."""

import logging
import os
import smtplib
from email.headerregistry import Address
from email.message import EmailMessage
from mako.template import Template


def default_email_variables():
    """Retrieve global values for Email provider."""
    return dict(
        BASE_PATH_TEMPLATES=os.getenv('BASE_PATH_TEMPLATES', '{}/bdc_core/email/templates'.format(os.getcwd())),
        EMAIL_ADDRESS=os.getenv('EMAIL_ADDRESS', 'test@domain.com'),
        EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD', 'password'),
        SMTP_PORT=os.getenv('SMTP_PORT', '587'),
        SMTP_HOST=os.getenv('SMTP_HOST', 'smtp.domain.com')
    )


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
        env = default_email_variables()
        env.update(kwargs)

        self.env = env

        self.to = self.mount_user(username, email_addr)
        self.email_msg = self.mount_email(
            template,
            subject,
            kwargs.pop('body_args', dict()),
            **kwargs
        )

    def mount_user(self, name, email_addr) -> Address:
        """Mount user recipient object."""
        return Address(display_name=name, addr_spec=email_addr)

    def mount_email(self, template, subject, args, **kwargs) -> EmailMessage:
        """Mount email recipient object."""

        template = Template(filename='{}/{}'.format(
            self.env['BASE_PATH_TEMPLATES'], template))
        text = template.render(args=args)

        msg = EmailMessage()

        msg['From'] = self.env['EMAIL_ADDRESS']
        msg['To'] = self.to
        msg['Subject'] = subject
        msg.set_content(text, subtype='html')

        return msg

    def send(self):
        """Dispatch email."""
        try:
            with smtplib.SMTP(self.env['SMTP_HOST'], port=int(self.env['SMTP_PORT'])) as smtp_server:
                smtp_server.ehlo()
                smtp_server.starttls()
                smtp_server.login(self.env['EMAIL_ADDRESS'], self.env['EMAIL_PASSWORD'])
                smtp_server.send_message(self.email_msg)
            return True
        except smtplib.SMTPException as e:
            logging.error(str(e))
            return False
