import os
from dotenv import load_dotenv


class Config:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

        PROXY = os.getenv('PROXY')
        LOGIN = os.getenv('LOGIN')
        PASSWORD = os.getenv('PASSWORD')
