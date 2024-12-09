import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    AI_PORT = os.getenv('AI_PORT')
    APP_PORT = os.getenv('APP_PORT')
    HOST = os.getenv('HOST')
    DEBUG = True
