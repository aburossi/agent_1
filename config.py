# config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment.")

# OpenAI Model Configuration
MODEL_CONFIG = {
    "temperature": 0,   # Control randomness
    "max_tokens": 150   # Limit output length
}
