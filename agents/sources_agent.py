# agents/sources_agent.py
import env_setup
from config import OPENAI_API_KEY, MODEL_CONFIG
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# Initialize the LLM using centralized config
llm = OpenAI(openai_api_key=OPENAI_API_KEY, **MODEL_CONFIG)

# Define the prompt template for the sources slide
sources_prompt_template = """
You are an expert researcher. Based on the following source text:
"{source_text}"
Generate a JSON object for the sources slide that follows this schema:
{
  "slide_type": "sources",
  "main_source": "<Primary source title and URL>",
  "additional_sources": [
    {"title": "<Source 2 title>", "url": "<Source 2 URL>"},
    {"title": "<Source 3 title>", "url": "<Source 3 URL>"},
    {"title": "<Source 4 title>", "url": "<Source 4 URL>"}
  ]
}
Ensure the JSON is valid and contains no additional text.
"""

# Create the LLMChain for the sources slide
sources_chain = PromptTemplate(
    template=sources_prompt_template,
    input_variables=["source_text"]
) | llm

