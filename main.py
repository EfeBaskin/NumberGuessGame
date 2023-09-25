#number guessing game with python
import random

print("welcome to the number guess game..".upper())

def guess():

    WannaPlay = input("wanna play yes/no :  ")

    while WannaPlay == "yes":

        compGuess=random.randint(1,50)

        difGame=str(input("choose a difficulty (easy or hard)  : \n "))

        guess=int(input("enter your guess 1-50 :"))
        turn=1

        if difGame == "hard":
            while guess!=compGuess and turn<5:
                if guess>compGuess:
                    print("lower your number!")
                    guess = int(input("enter your guess 1-50 :"))

                elif guess<compGuess:
                    print("upper your number!")
                    guess=int(input("enter your guess 1-50 :"))
                    turn+=1

                elif guess==compGuess:
                    print(f"Congrats you did it.Number : {compGuess}")

                if turn==5 :
                    print("out of turns sadly :( number was {}".format(compGuess))
                    WannaPlay=input("Play Again : 'yes','no'\n ")
                    continue

        elif difGame== "easy":

            while guess!=compGuess and turn<10:

                if guess>compGuess:
                    print("lower your number!")
                    guess = int(input("enter your guess 1-50 :"))

                elif guess<compGuess:
                    print("upper your number!")
                    guess=int(input("enter your guess 1-50 :"))
                    turn+=1

                if  turn==10 :
                    print("out of turns sadly :( number was {}".format(compGuess))

                elif guess==compGuess:
                    print(f"Congrats you did it.Number : {compGuess}")
                    WannaPlay = input("do you wanna play again : \n")
                    continue
    while WannaPlay == "no":
        print("see you later..")
        break
guess()
