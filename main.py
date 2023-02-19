import random

# ROCK PAPER SCISSORS
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

# 0 beats 2 but not beats 1
# 1 beats 0 but not beats 2
# 2 beats 1 but not beats 0
theTools = [rock, paper, scissors]

yourChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if yourChoice >=3 or yourChoice < 0:
    print("You typed an invalid number, you loser!")
else:
    print(f"You choosed {yourChoice}" + theTools[yourChoice])

    computerChoice = random.randint(0, 2)
    print(f"Computer choosed {computerChoice}" + theTools[computerChoice])

    if computerChoice == 0 and yourChoice == 2:
        print("You lose")
    elif computerChoice == 0 and yourChoice == 1:
        print("You won")
    elif computerChoice == 1 and yourChoice == 0:
        print("You lose")
    elif computerChoice == 1 and yourChoice == 2:
        print("You won")
    elif computerChoice == 2 and yourChoice == 1:
        print("You lose")
    elif computerChoice == 2 and yourChoice == 0:
        print("You won")
    else: print("It's a draw")