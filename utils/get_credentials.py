# pip install python-dotenv
import os
from dotenv import load_dotenv, find_dotenv


class Credentials:

    def __init__(self):
        load_dotenv(find_dotenv())

        self.first_login = os.getenv('FIRST_LOGIN')
        self.kp_login = os.getenv('KP_LOGIN')
        self.kp_password = os.getenv('KP_PASSWORD')

