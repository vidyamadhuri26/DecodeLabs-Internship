import json
from pathlib import Path

from src.gemini_client import ask_gemini


def classify_complaint(customer_data):
    """
    Classifies a customer complaint and returns routing information.
    """

    prompt_path = Path("prompts/classification_prompt.txt")
    prompt = prompt_path.read_text(encoding="utf-8")

    final_prompt = prompt.replace(
        "{CUSTOMER_DATA}",
        json.dumps(customer_data, indent=2)
    )

    response = ask_gemini(final_prompt)

    return json.loads(response)