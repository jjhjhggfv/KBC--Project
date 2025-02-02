# main.py

from game_logic import play_game

if __name__ == "__main__":
    print("Welcome to Kaun Banega Crorepati!")
    user_name = input("Please enter your name: ").strip().title()
    play_game(user_name)
