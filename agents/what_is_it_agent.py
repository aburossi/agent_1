# agents/what_is_it_agent.py
import env_setup  # Ensure environment variables are loaded
import os
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# Retrieve API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment.")

# Initialize the LLM
llm = OpenAI(temperature=0, max_tokens=150, openai_api_key=OPENAI_API_KEY)

# Define the prompt template for the "What is it?" slide
what_is_it_prompt_template = """
You are an expert content creator. Based on the following source text:
"{source_text}"
Generate a JSON object in italian for the "What is it?" slide that follows this schema:
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

# Create the LLMChain for the "What is it?" slide
what_is_it_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template=what_is_it_prompt_template,
        input_variables=["source_text"]
    )
)
