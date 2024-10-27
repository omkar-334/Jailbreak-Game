import os
import random
import re

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_models = [
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-4-turbo",
    "gpt-4",
    "gpt-3.5-turbo",
    "o1-preview",
    "o1-mini",
]
models = [line.strip() for line in open("models.txt", "r") if line.strip()]


def llm(system_prompt: str, user_prompt: str, model) -> str:
    client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        stop=None,
        stream=False,
        model=model,
    )

    return chat_completion.choices[0].message.content


def clean(text):
    try:
        text = text.strip().strip('"').strip("'")
        sentences = re.findall(r"[^.!?]+[.!?]", text)
        text = "".join(sentences)
    except Exception:
        pass
    return text
