import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools.basic import get_time, calculate

load_dotenv()

MODEL = "gemini-3-flash-preview"
SYSTEM_PROMPT = (
    "You are FRIDAY, a personal AI assistant. Be concise and helpful. "
    "Use your tools whenever they give a more accurate answer."
)


class Brain:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = self.client.chats.create(
            model=MODEL,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[get_time, calculate],
            ),
        )

    def ask(self, text: str) -> str:
        return self.chat.send_message(text).text