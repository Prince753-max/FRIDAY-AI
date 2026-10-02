from core.brain import Brain
from voice.ears import record
from voice.mouth import speak


def main():
    brain = Brain()
    print("FRIDAY online. Press Enter to talk, or type a message. 'exit' to quit.")
    while True:
        user = input("You (Enter = speak): ").strip()
        if user.lower() in ("exit", "quit"):
            break
        try:
            if user == "":
                print("Listening for 5 seconds...")
                reply = brain.ask_audio(record(5))
            else:
                reply = brain.ask(user)
            print("FRIDAY:", reply)
            speak(reply)
        except Exception as e:
            print("Error:", e)


main()