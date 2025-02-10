import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Updated imports per deprecation warnings:
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI  # Use the updated langchain-openai package

# Initialize the LLM with the API key and desired parameters
llm = OpenAI(temperature=0, max_tokens=150, openai_api_key=OPENAI_API_KEY)

# --- Agent Prompt Templates ---

# Title Slide Agent
title_prompt_template = """
You are an expert content creator. Based on the following source text:
"{source_text}"
Generate a JSON object for the title slide that follows this schema:
{{
  "slide_type": "title",
  "title": "<Main Title Here>",
  "subtitle": "<Subtitle Here>",
  "image_url": "<Image URL or empty>"
}}
Ensure the JSON is valid and contains no additional text.
"""

# Sources Slide Agent
sources_prompt_template = """
You are an expert researcher. Based on the following source text:
"{source_text}"
Generate a JSON object for the sources slide that follows this schema:
{{
  "slide_type": "sources",
  "main_source": "<Primary source title and URL>",
  "additional_sources": [
    {{"title": "<Source 2 title>", "url": "<Source 2 URL>"}},
    {{"title": "<Source 3 title>", "url": "<Source 3 URL>"}},
    {{"title": "<Source 4 title>", "url": "<Source 4 URL>"}}
  ]
}}
Ensure the JSON is valid and contains no additional text.
"""

# "What is it?" Slide Agent
what_is_it_prompt_template = """
You are an expert content creator. Based on the following source text:
"{source_text}"
Generate a JSON object for the "What is it?" slide that follows this schema:
{{
  "slide_type": "content",
  "section": "what_is_it",
  "heading": "What is it?",
  "content": "<Detailed explanation here>",
  "image_url": "<Relevant image URL or empty>",
  "references": []
}}
Ensure the JSON is valid and contains no additional text.
"""

# --- Create LLMChains for Each Agent ---

title_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template=title_prompt_template,
        input_variables=["source_text"]
    )
)

sources_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template=sources_prompt_template,
        input_variables=["source_text"]
    )
)

what_is_it_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template=what_is_it_prompt_template,
        input_variables=["source_text"]
    )
)

# Helper function to extract and parse the output
def parse_output(output):
    # If output is a dict and contains a "text" key, use that value.
    if isinstance(output, dict) and "text" in output:
        output = output["text"]
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw_output": output}

# --- Central Orchestrator Function ---

def orchestrate_slide_deck(source_text: str) -> dict:
    slides = []

    # Title Slide
    title_output = title_chain.invoke({"source_text": source_text})
    title_json = parse_output(title_output)
    slides.append(title_json)

    # Sources Slide
    sources_output = sources_chain.invoke({"source_text": source_text})
    sources_json = parse_output(sources_output)
    slides.append(sources_json)

    # "What is it?" Slide
    what_is_it_output = what_is_it_chain.invoke({"source_text": source_text})
    what_is_it_json = parse_output(what_is_it_output)
    slides.append(what_is_it_json)

    # Aggregate all slide outputs into a single deck JSON document
    deck = {"deck": slides}
    return deck

# --- Testing the Pipeline ---

if __name__ == "__main__":
    # Example source text for testing
    source_text = "This is a sample source text used to generate a simple slide deck using LangChain."
    
    # Run the orchestrator to generate the slide deck JSON
    slide_deck = orchestrate_slide_deck(source_text)
    
    # Output the final JSON in a readable format
    print(json.dumps(slide_deck, indent=2))
