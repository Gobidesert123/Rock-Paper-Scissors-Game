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

# Write your code below this line 👇
from random import randint

# Player choice
diff_choices = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Computers choice
computer_choice = randint(0, 2)
# Declaring the winner
if choice == 0 and computer_choice == 0:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("Tie")

elif choice == 0 and computer_choice == 1:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("Computer wins")

elif choice == 0 and computer_choice == 2:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("You win")

elif choice == 1 and computer_choice == 0:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print('You win')

elif choice == 1 and computer_choice == 1:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("Tie")

elif choice == 1 and computer_choice == 2:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("Computer wins")

elif choice == 2 and computer_choice == 0:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("Computer wins")

elif choice == 2 and computer_choice == 1:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("You win")

elif choice == 2 and computer_choice == 2:
    print("Your choice;")
    print(diff_choices[choice])

    print("Computers Choice:")
    print(diff_choices[computer_choice])
    print("Tie")
else:
    print("You have chosen an invalid option")










