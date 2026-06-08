import ollama

def extract_action_items(transcript):

    prompt = f"""
You are an AI meeting assistant.

Extract all action items, tasks, assignments, deadlines,
and responsibilities from the meeting transcript.

Return only a bullet list.

Transcript:
{transcript}
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]