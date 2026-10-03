from core.brain import Brain
from voice.ears import record
from voice.mouth import speak
from voice.wake import listen_for_wake_word


def main():
    brain = Brain()
    print("FRIDAY is running in the background. Say 'Hey Jarvis' to wake it.")
    while True:
        listen_for_wake_word("hey_jarvis")
        speak("Yes?")
        print("Listening for your request...")
        reply = brain.ask_audio(record(5))
        print("FRIDAY:", reply)
        speak(reply)


main()