# agents/what_is_it_agent.py
import env_setup
from config import OPENAI_API_KEY, MODEL_CONFIG
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# Initialize the LLM using centralized config
llm = OpenAI(openai_api_key=OPENAI_API_KEY, **MODEL_CONFIG)

# Define the prompt template for the "What is it?" slide
what_is_it_prompt_template = """
You are an expert content creator. Based on the following source text:
"{source_text}"
Generate a JSON object for the "What is it?" slide that follows this schema:
{
  "slide_type": "content",
  "section": "what_is_it",
  "heading": "What is it?",
  "content": "<Detailed explanation here>",
  "image_url": "<Relevant image URL or empty>",
  "references": []
}
Ensure the JSON is valid and contains no additional text.
"""

# Create the LLMChain for the "What is it?" slide
title_chain = PromptTemplate(
    template=what_is_it_prompt_template,
    input_variables=["source_text"]
) | llm

