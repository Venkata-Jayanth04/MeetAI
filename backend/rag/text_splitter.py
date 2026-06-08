import re

def split_text(text, max_chunk_size=200):

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_chunk = ""

    for sentence in sentences:

        if not sentence.strip():
            continue

        if len(current_chunk) + len(sentence) <= max_chunk_size:

            if current_chunk:
                current_chunk += " "

            current_chunk += sentence

        else:

            if current_chunk:
                chunks.append(current_chunk)

            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    return chunks