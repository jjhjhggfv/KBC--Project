# game_logic.py

import random
from data import questions

def use_lifeline(question):
    """Provides a 50-50 lifeline by removing two incorrect options."""
    correct_option = question["answer"]
    options = question["options"]
    wrong_option = random.choice([opt for opt in options if opt != correct_option])
    lifeline_options = [correct_option, wrong_option]
    random.shuffle(lifeline_options)
    return lifeline_options

def play_game(user_name):
    """Runs the main gameplay loop."""
    prize_money = [1000, 5000, 10000, 20000, 50000]
    total_prize = 0
    lifeline_used = False

    print(f"\nWelcome to Kaun Banega Crorepati, {user_name}!")
    print("Answer the questions correctly to win prize money!\n")

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for idx, option in enumerate(question["options"], start=1):
            print(f"{idx}. {option}")
        print("\n")

        if not lifeline_used:
            print("Type 'lifeline' to use the 50-50 lifeline (only once).")
        user_input = input("Enter your answer (1/2/3/4) or 'lifeline': ").strip()

        if user_input.lower() == "lifeline" and not lifeline_used:
            lifeline_used = True
            lifeline_options = use_lifeline(question)
            print("Lifeline Options:")
            for idx, option in enumerate(lifeline_options, start=1):
                print(f"{idx}. {option}")
            user_input = input("Choose your answer (1/2): ").strip()
            selected_option = lifeline_options[int(user_input) - 1]
        elif user_input.isdigit() and 1 <= int(user_input) <= 4:
            selected_option = question["options"][int(user_input) - 1]
        else:
            print("Invalid input. You lose!")
            break

        if selected_option == question["answer"]:
            print(f"Correct! You have won ₹{prize_money[i]}.\n")
            total_prize = prize_money[i]
        else:
            print(f"Wrong answer! The correct answer was {question['answer']}.")
            break

    print(f"Game Over, {user_name}! You won a total of ₹{total_prize}.")
    print("Thank you for playing Kaun Banega Crorepati!")
