from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="what is colour of apple?",
)

print(response.text)