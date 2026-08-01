import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt, model="gemini-3.5-flash-lite"):
    """
    Sends a prompt to Gemini and returns the text response.
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text