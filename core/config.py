import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')
    DEBUG = True
