import random


class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        user_choice = input("Please enter rock , paper or scissors")

        while (user_choice != 'rock' or user_choice != 'paper' or user_choice != 'scissors'):
            user_choice = input("Please input rock ,paper or scissors not something else !!!!")

        return user_choice

    def get_computer_item(self):
        return random.choice("rock", "paper", "scissors")

    def get_game_result(self, user_item, computer_item):
        user_item = get_user_item()
        computer_item = get_computer_item()
        win = 0;

        while (win != 1):
            if (user_item == "scissors" and computer_item == "paper"):
                print(f"You win the computer choice{computer_item}, You WIN !!!")
                count += 1

            elif (user_item == "paper" and computer_item == "rock"):
                print(f"You win the computer choice{computer_item}, You WIN !!!")
                count += 1

            elif (user_item == "rock" and computer_item == "scissors"):
                print(f"You win the computer choice{computer_item}, You WIN !!!")
                count += 1

            elif (user_item == "scissors" and computer_item == "rock"):
                print(f"You lose the computer choice{computer_item}, You LOSE !!!")
                count += 1

            elif (user_item == "paper" and computer_item == "scissors"):
                print(f"You lose the computer choice{computer_item}, You LOSE !!!")
                count += 1

            elif (user_item == "rock" and computer_item == "paper"):
                print(f"You lose the computer choice{computer_item}, You LOSE !!!")
                count += 1

            elif (user_item == "rock" and computer_item == "rock"):
                print("Egality")
                user_item = get_user_item()
                computer_item = get_computer_item()


            elif (user_item == "paper" and computer_item == "paper"):
                print("Egality")
                user_item = get_user_item()
                computer_item = get_computer_item()

            elif (user_item == "scissors" and computer_item == "scissors"):
                print("Egality")
                user_item = get_user_item()
                computer_item = get_computer_item()

    def play(self):
        user_item = get_user_item()
        computer_item = get_computer_item()
        get_game_result(user_item, computer_item)
