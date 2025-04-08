import random
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def magic_8_ball():
    clear_console()
    print("🎱 Welcome to the Magic 8 Ball!")
    print("-" * 35)

    question = input("📝 What’s your question? ")

    print("\n🔮 Shaking the ball", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    responses = [
        "Yes - definitely.",
        "It is decidedly so.",
        "Without a doubt.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    answer = random.choice(responses)
    print(f"\n\n🎲 Magic 8 Ball says: {answer}")

if __name__ == "__main__":
    magic_8_ball()
