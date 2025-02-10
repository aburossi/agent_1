# env_setup.py
from pathlib import Path
from dotenv import load_dotenv

# Explicitly define the path to the .env file (assumes .env is in the same directory as env_setup.py)
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)
