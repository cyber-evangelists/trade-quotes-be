import os

from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.environ['DB_HOST']
SMTP_PWD = os.environ['SMTP_PWD']
