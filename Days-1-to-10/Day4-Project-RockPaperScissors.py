rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_var = [rock, paper, scissors]

user_choice = int(
    input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number, you lose!")
else:
    print(game_var[user_choice])

    print("Computer chose:")
    random_choice = random.randint(0, 2)
    print(game_var[random_choice])

    if user_choice == 0 and random_choice == 2 or user_choice == 2 and random_choice == 1 or user_choice == 1 and random_choice == 0:
        print("You win")
    elif user_choice == random_choice:
        print("It's a draw!")
    else:
        print("You lose")
