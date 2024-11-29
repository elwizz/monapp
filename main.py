# Tiny Rock-paper-scissors game for OY CSc Orientation course 2024 Docker exercise
import random


def checker(draw):
    if draw.lower() == "rock" or draw.lower() == "paper" or draw.lower() == "scissors":
        return True
    elif draw.lower() == "quit":
        quit()
    else:
        return False


def playit(play):
    playerhand = play.lower()
    games = ("rock", "scissors", "paper")
    thisgame = games[random.randint(0, 2)]

    if playerhand == thisgame:
        return 0
    elif ((playerhand == "paper" and thisgame == "scissors") or (playerhand == "rock" and thisgame == "paper") or
          (playerhand == "scissors" and thisgame == "rock")):
        return 1
    else:
        return 2


if __name__ == '__main__':
    while True:
        thishand = input("Paper, rock, scissors or quit? >\n ")
        while not checker(thishand):
            thishand = (input("Paper, rock or scissors or quit >\n "))
        thisplay = playit(thishand)
        if thisplay == 0:
            print("It's a draw!")
        elif thisplay == 1:
            print("You lose!")
        elif thisplay == 2:
            print("You win!")
