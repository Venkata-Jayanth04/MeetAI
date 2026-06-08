from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_text(text):

    prompt = f"Summarize this meeting transcript:\n{text}"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=120,
        min_length=30,
        num_beams=4
    )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary