import json
from pathlib import Path

from src.gemini_client import ask_gemini


def extract_customer_data(email_text):
    """
    Extract structured customer information from a support email.
    """

    # Read the prompt template
    prompt_path = Path("prompts/extraction_prompt.txt")
    prompt = prompt_path.read_text(encoding="utf-8")

    # Replace placeholder with actual email
    final_prompt = prompt.replace("{EMAIL_TEXT}", email_text)

    # Send prompt to Gemini
    response = ask_gemini(final_prompt)

    # Convert JSON string into Python dictionary
    return json.loads(response)