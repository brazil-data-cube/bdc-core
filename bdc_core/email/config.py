import os

BASE_PATH_TEMPLATES = os.getenv('BASE_PATH_TEMPLATES', 'templates')

SMTP_PORT = os.getenv('SMTP_PORT', 587)
SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.domain.com')

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'test@domain.com')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'password')
