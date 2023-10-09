import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    ALCHEMY_API_URL = os.getenv("ALCHEMY_API_URL")