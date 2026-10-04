import pyttsx3


def speak(text: str) -> None:
    """Speaks text aloud using the local TTS engine."""
    clean = text.replace("*", "").replace("#", "").replace("`", "")
    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    engine.say(clean)
    engine.runAndWait()
    engine.stop()