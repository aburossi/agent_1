import json

def parse_output(output):
    # If output is a dict and contains a "text" key, extract that value.
    if isinstance(output, dict) and "text" in output:
        output = output["text"]
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw_output": output}
