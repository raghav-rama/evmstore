import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
    PRIVATE_KEY = os.getenv("PRIVATE_KEY")
