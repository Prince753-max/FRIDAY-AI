from core.brain import Brain
from voice.ears import record
from voice.mouth import speak
from voice.wake import listen_for_wake_word

import sys

log_file = open("friday.log", "a", encoding="utf-8", buffering=1)
sys.stdout = log_file
sys.stderr = log_file


def main():
    brain = Brain()
    print("FRIDAY is running in the background. Say 'Hey Jarvis' to wake it.")
    while True:
        listen_for_wake_word("hey_jarvis")
        speak("Yes?")
        print("Listening for your request...")
        try:
            reply = brain.ask_audio(record(4))
            print("FRIDAY:", reply)
            speak(reply)
        except Exception as e:
            print("Error:", e)
            speak("Sorry, I ran into a problem. Please try again.")


main()