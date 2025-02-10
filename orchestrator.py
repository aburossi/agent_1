from agents.title_agent import title_chain
from agents.sources_agent import sources_chain
from agents.what_is_it_agent import what_is_it_chain
from utils import parse_output

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

    return {"deck": slides}