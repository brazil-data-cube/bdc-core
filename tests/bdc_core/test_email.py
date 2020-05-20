import unittest
from unittest.mock import MagicMock, patch
from bdc_core.email.business import EmailBusiness, is_valid_smtp


class TestSendEmail(unittest.TestCase):
    def setUp(self):
        self.email = EmailBusiness(
            username='Full Name',
            email_addr='username@domain.com',
            subject='Title',
            template='example.txt',
            body_args=dict(
                title_page='BDC Send-email',
                title_body='Welcome',
                body='Hello World!!!',
                button_title='Go to page',
                button_link='http://brazildatacube.org'
            )
        )

    def test_create_obj(self):
        self.assertNotEqual(self.email.to, None)
        self.assertNotEqual(self.email.email_msg, None)

    @patch('smtplib.SMTP')
    def test_is_valid_smtp(self, mock_smtp):
        mock_smtp_instance = MagicMock()

        mock_smtp.return_value.__enter__ = mock_smtp_instance

        host = 'myemailserver'
        email = 'test@awesome.email.com'
        port = 587
        password = 'testpass'

        res = is_valid_smtp(host, port, email, password)

        self.assertTrue(res)
        mock_smtp.assert_called_with(host, port=port)
        # Must call login with expected values
        mock_smtp_instance.return_value.login.assert_called_with(email, password)
