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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print("Choose :,\n" \
# "Paper for 2 ,\n" \
# "Scissor for 3 ,\n")
game_images = [rock,paper,scissor]

user_choice = int(input("Choices :  Rock for 0 , Paper for 1 , Scissor for 2 \n"))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer Choice :")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice >= 3 or user_choice < 0 :
    print("Invalid!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Draw!")
