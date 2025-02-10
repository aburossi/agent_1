import json
from dotenv import load_dotenv
import os
from orchestrator import orchestrate_slide_deck

# Explicitly load .env file
load_dotenv()

def main():
    source_text = "This is a sample source text used to generate a simple slide deck using LangChain."
    
    # Check if the API key is loaded
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is still not found in environment after loading .env.")

    slide_deck = orchestrate_slide_deck(source_text)
    print(json.dumps(slide_deck, indent=2))

if __name__ == '__main__':
    main()
