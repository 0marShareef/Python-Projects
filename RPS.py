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
rps = [rock, paper, scissors]
comp_choice = random.choice(rps)
prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if prompt != 0 and prompt != 1 and prompt != 2:
    print("Invalid input.")
    quit()
human_choice = rps[prompt]
print(f"You chose:\n{human_choice}")

print(f"Computer chose:\n{comp_choice}")
if human_choice == rock and comp_choice == paper:
    print("You lose.")
elif human_choice == paper and comp_choice == rock:
    print("You win!")
elif human_choice == paper and comp_choice == scissors:
    print("You lose.")
elif human_choice == scissors and comp_choice == paper:
    print("You win!")
elif human_choice == scissors and comp_choice == rock:
    print("You lose!")
elif human_choice == rock and comp_choice == scissors:
    print("You win!")
elif human_choice == comp_choice:
    print("It's a draw!")
