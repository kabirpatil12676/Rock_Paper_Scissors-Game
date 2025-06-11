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

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])

computer_input = random.randint(0,2)
print("Computers Choice:")
print(game_images[computer_input])

if user_input >= 3:
    print("You Entered Inavlid Number YOU Lose")
elif user_input == computer_input:
    print("It's a Draw!")
elif user_input > computer_input:
    print("You Win!")
elif user_input < computer_input:
    print("You Lose!")

elif user_input == 0 and computer_input == 2:
    print("You Win!")
elif computer_input == 0 and user_input == 2:
    print("You Win!")