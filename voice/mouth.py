import os
import subprocess


def speak(text: str) -> None:
    """Speaks text aloud using the built-in Windows voice."""
    clean = text.replace("*", "").replace("#", "").replace("`", "")
    env = dict(os.environ, FRIDAY_TEXT=clean)
    cmd = (
        "Add-Type -AssemblyName System.Speech; "
        "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        "$s.Speak($env:FRIDAY_TEXT)"
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", cmd], env=env)