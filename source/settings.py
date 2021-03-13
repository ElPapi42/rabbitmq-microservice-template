import os
import pathlib

from dotenv import load_dotenv


# Load .env vars
dotenv_path = pathlib.Path('.').parent/'.env'
load_dotenv(dotenv_path)

RABBIT_URL = os.environ.get('RABBIT_URL')
