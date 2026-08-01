from pathlib import Path

from src.gemini_client import ask_gemini


def get_policy_decision(customer_data):
    """
    Uses the company policy to answer the customer's case.
    """

    # Read company policy
    policy = Path("dataset/company_policy.txt").read_text(
        encoding="utf-8"
    )

    # Read prompt
    prompt = Path("prompts/rag_prompt.txt").read_text(
        encoding="utf-8"
    )

    # Replace placeholders
    final_prompt = prompt.replace(
        "{COMPANY_POLICY}",
        policy
    )

    final_prompt = final_prompt.replace(
        "{CUSTOMER_DATA}",
        str(customer_data)
    )

    # Ask Gemini
    return ask_gemini(final_prompt)