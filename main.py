import random

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

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!")
elif player_choice == 0:
    print(options[player_choice])
    print("Computer chose:\n" + options[computer_choice])
    if computer_choice == 0:
        print("It's a draw!")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("You win!")
elif player_choice == 1:
    print(options[player_choice])
    print("Computer chose:\n" + options[computer_choice])
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("Its a draw!")
    else:
        print("You lose")
else:
    print(options[player_choice])
    print("Computer chose:\n" + options[computer_choice])
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    else:
        print("It's a draw!")