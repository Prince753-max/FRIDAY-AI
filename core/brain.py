import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools.basic import get_time, calculate
from tools.gcal import list_events, create_event

load_dotenv()

MODEL = "gemini-3-flash-preview"
SYSTEM_PROMPT = (
    "You are FRIDAY, a personal AI assistant. Be concise and helpful. "
    "Use your tools whenever they give a more accurate answer. "
    "Before creating or changing anything (events, emails), state the exact "
    "details and ask the user to confirm. Only call the tool after they say yes. "
    "Use get_time to work out dates like 'tomorrow'."
)


class Brain:
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = self.client.chats.create(
            model=MODEL,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[get_time, calculate, list_events, create_event],
            ),
        )

    def ask(self, text: str) -> str:
        return self.chat.send_message(text).text

    def ask_audio(self, wav_bytes: bytes) -> str:
        part = types.Part.from_bytes(data=wav_bytes, mime_type="audio/wav")
        prompt = "The user is speaking to you in this audio. Reply to them."
        return self.chat.send_message([part, prompt]).text