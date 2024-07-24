import random

def gtn():
    num =random.randint(1,100)
    attempts=0

    while True:
        guess=int(input("Guess the num between 1 to 100"))
        attempts +=1

        if guess<num:
            print("too low")
        elif guess>num:
            print("too high")
        else:
            print(f"yipeee you guessed the number in {attempts} attempts")
            break
gtn()          