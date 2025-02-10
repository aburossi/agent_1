import os
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# Ensure the API key is available (it should be loaded via your .env in main.py)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment.")

# Initialize the LLM
llm = OpenAI(temperature=0, max_tokens=150, openai_api_key=OPENAI_API_KEY)

# Define the prompt template for the title slide
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

# Create the LLMChain for the title slide
title_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        template=title_prompt_template,
        input_variables=["source_text"]
    )
)
