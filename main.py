import json
from dotenv import load_dotenv
import os
from orchestrator import orchestrate_slide_deck

def main():
    # Example source text for testing
    source_text = "This is a sample source text used to generate a simple slide deck using LangChain."
    # Run the orchestrator to generate the slide deck JSON
    slide_deck = orchestrate_slide_deck(source_text)
    # Print the final JSON output in a readable format
    print(json.dumps(slide_deck, indent=2))

if __name__ == '__main__':
    main()
