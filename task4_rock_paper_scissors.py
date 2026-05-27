"""
CODSOFT Python Internship - Task 4
Rock-Paper-Scissors Game
"""

import random

CHOICES = ["rock", "paper", "scissors"]
EMOJIS  = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if wins[user] == computer else "computer"

def display_scores(scores):
    print(f"\n  📊 Score | You: {scores['user']}  "
          f"Computer: {scores['computer']}  "
          f"Ties: {scores['ties']}")

def main():
    print("\n" + "="*45)
    print("    🎮 ROCK - PAPER - SCISSORS GAME")
    print("="*45)

    scores = {"user": 0, "computer": 0, "ties": 0}
    round_num = 0

    while True:
        print(f"\n--- Round {round_num + 1} ---")
        print("Choose:  1. Rock 🪨   2. Paper 📄   3. Scissors ✂️   4. Quit")

        choice = input("Your choice: ").strip()

        if choice == "4" or choice.lower() == "quit":
            break

        # Accept number or text input
        if choice == "1" or choice.lower() == "rock":
            user_choice = "rock"
        elif choice == "2" or choice.lower() == "paper":
            user_choice = "paper"
        elif choice == "3" or choice.lower() == "scissors":
            user_choice = "scissors"
        else:
            print("❌ Invalid choice! Enter 1, 2, 3, or 4.")
            continue

        computer_choice = random.choice(CHOICES)
        round_num += 1

        print(f"\n  You chose:      {EMOJIS[user_choice]}  {user_choice.capitalize()}")
        print(f"  Computer chose: {EMOJIS[computer_choice]}  {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("  🤝 It's a TIE!")
            scores["ties"] += 1
        elif result == "user":
            print("  🎉 You WIN this round!")
            scores["user"] += 1
        else:
            print("  💻 Computer WINS this round!")
            scores["computer"] += 1

        display_scores(scores)

        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != "y":
            break

    # Final summary
    print("\n" + "="*45)
    print("         🏁 FINAL RESULTS")
    print("="*45)
    display_scores(scores)
    total = scores["user"] + scores["computer"] + scores["ties"]
    if total > 0:
        if scores["user"] > scores["computer"]:
            print("  🏆 Overall Winner: YOU!")
        elif scores["computer"] > scores["user"]:
            print("  🏆 Overall Winner: COMPUTER!")
        else:
            print("  🏆 Overall Result: It's a DRAW!")
    print("="*45)
    print("👋 Thanks for playing!")

if __name__ == "__main__":
    main()
