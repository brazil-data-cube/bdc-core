import unittest
from bdc_core.email.business import EmailBusiness


class TestSendEmail(unittest.TestCase):
    def setUp(self):
        self.email = EmailBusiness(
            username='Full Name', 
            email_addr='username@domain.com', 
            subject='Title',
            template='example', 
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

    def test_send_email(self):
        result = self.email.send()
        self.assertEqual(result, True)