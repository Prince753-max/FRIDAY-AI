from core.brain import Brain


def main():
    brain = Brain()
    print("FRIDAY online. Type 'exit' to quit.")
    while True:
        user = input("You: ").strip()
        if user.lower() in ("exit", "quit"):
            break
        if not user:
            continue
        try:
            print("FRIDAY:", brain.ask(user))
        except Exception as e:
            print("Error:", e)


main()