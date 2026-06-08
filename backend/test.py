from nlp.ner import extract_entities

text = """
Ravi will submit the report tomorrow.

Google is developing AI systems.

Microsoft is investing heavily in LLMs.

The meeting will be held in Hyderabad.
"""

result = extract_entities(text)

print(result)