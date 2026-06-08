import ollama


def ask_llm(context, question):

    prompt = f"""
You are an intelligent meeting assistant.

Use ONLY the provided meeting context.

Meeting Context:
{context}

Question:
{question}

Answer:
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