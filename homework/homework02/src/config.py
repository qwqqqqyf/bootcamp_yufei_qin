import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()

def get_key():
    return os.getenv("API_KEY")

print(get_key())