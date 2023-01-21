import os
from dotenv import load_dotenv

load_dotenv()

REGEX = os.getenv('REGEX')
FILE_PATH = os.getenv('FILE_PATH')
HEAD = os.getenv('HEAD')

