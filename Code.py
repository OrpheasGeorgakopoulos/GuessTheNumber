import random
from logging.config import stopListening

lives = 5
guess = 101
number = random.randint(0,100)

while guess != number and lives>0:
    guess = int(input("Guess the number between 0 and 100: "))
    if guess<number:
        print("Up!")
        lives = lives -1
    elif guess>number:
        print("Down!")
        lives = lives -1
    else:
        print("Good Job! Correct Number!")
    print("Lives: ", lives)
    if lives<1:
        print("You lost!")
        print("Correct Number: ", number)
