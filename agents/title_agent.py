# agents/title_agent.py
import env_setup  # Ensure environment variables are loaded
from config import OPENAI_API_KEY, MODEL_CONFIG
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

# Initialize the LLM using centralized config
llm = OpenAI(openai_api_key=OPENAI_API_KEY, **MODEL_CONFIG)

# Define the prompt template for the title slide
title_prompt_template = """
You are an expert content creator. Based on the following source text:
"{source_text}"
Generate a JSON object for the title slide that follows this schema:
{
  "slide_type": "title",
  "title": "<Main Title Here>",
  "subtitle": "<Subtitle Here>",
  "image_url": "<Image URL or empty>"
}
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
