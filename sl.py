import time
import random

def Roll_dice():
    return random.randint(1,6)

def Move(Player, value, P1N, P2N, P3N, P4N):
    snake_squares = {11: 2, 25: 4, 38: 9, 65: 46, 89:70,93:64}
    ladder_squares = {8: 37, 13:34, 40: 68, 52:81, 76:97}
    Throw = Roll_dice()
    if Player == 1:
        num = value + Throw
        print(P1N, "Rolled a", Throw, "And is now on", num)
    if Player == 2:
        num = value + Throw
        print(P2N, "Rolled a", Throw, "And is now on", num)
    if Player == 3:
        num = value + Throw
    print(P3N, "Rolled a", Throw, "And is now on", num)
    if Player == 4:
        num = value + Throw
        print(P4N, "Rolled a", Throw, "And is now on", num)
    if num in snake_squares:
        print("Player got bitten by a snake and is now on square", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        print("Player climbed a ladder and is now on square", ladder_squares[num])
        num = ladder_squares[num]
    else:
        print("",end = "")
    return num

def Setup_Players():
    players=6
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 2:
                print("Must be less than 5 and greater than 1")
            else:
                return players
        except:
            print("Must be a number")



def Player_Names(NumP):
    Names = []
    for i in range(1,NumP+1):
        Names.append(input("What is the name of Player"+str(i)+"?"))
    Names.append("")
    return Names


Num_Players=Setup_Players()
P_Names = Player_Names(Num_Players)
P1N = 0
P2N = 0
P3N = 0
P4N = 0
for i in P_Names:
    if P1N == 0:
        P1N = i
        if Num_Players == 1:
            P2N, P3N, P4N = "", "", ""
            break
    elif P2N == 0:
        P2N = i
        if Num_Players == 2:
            P3N, P4N = "", ""
            break
    elif P3N == 0:
        P3N = i
        if Num_Players == 3:
            P4N = ""
            break
    elif P4N == 0:
        P4N = i
    else:
        break
print(P1N, P2N, P3N, P4N, ", Welcome To Snakes And Ladders")
input("Press Enter")
Num1 = 0
Num2 = 0
Num3 = 0
Num4 = 0
x = 0
while Num1 < 100 and Num2 < 100 and Num3 < 100 and Num4 < 100:       
    while x < Num_Players:
        x=x+1
        if x == 1:
            Num1 = Move(1, Num1, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num1 > 99:
                print(P1N, "WINS!")
                time.sleep(3)
                exit()
        if x == 2:
            Num2 = Move(2, Num2, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num2 > 99:
                print(P2N, "WINS!")
                time.sleep(3)
                exit()            
        if x == 3:
            Num3 = Move(3, Num3, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num3 > 99:
                print(P3N, "WINS!")
                time.sleep(3)
                exit()
        if x == 4:
            Num4 = Move(4, Num4, P1N, P2N, P3N, P4N)
            input("Press Enter")
            if Num4 > 99:
                print(P4N, "WINS!")
                time.sleep(3)
                exit()
    x=0

def setup_game():
    players=6
    while True:
        try:
            print("How many players are in the game?")
            players = int(input())
            if players > 4 or players < 2:
                print("Must be less than 5 and greater than 1")
            else:
                break
        except ValueError:
            print("Must be a number")

    names = {}
    for i in range(1,players+1):
        while True:
            name = input("What is the name of Player {}? ".format(i))
            if not name in names:
                names[name] = 0
                break
            else:
                print('Cannot have duplicate names')
    return names


def move_player(player, current_pos):
    snake_squares = {11: 2, 25: 4, 38: 9, 65: 46, 89:70,93:64}
    ladder_squares = {8: 37, 13:34, 40: 68, 52:81, 76:97}
    throw = roll_dice()
    next_pos = current_pos + throw
    print("{0} rolled a {1} and is now on {2}".format(player, throw, next_pos))

    if next_pos in snake_squares:
        print("Player got bitten by a snake and is now on square {}".format(snake_squares[next_pos]))
        next_pos = snake_squares[next_pos]
    elif next_pos in ladder_squares:
        print("Player climbed a ladder and is now on square {}".format(ladder_squares[next_pos]))
        next_pos = ladder_squares[next_pos]
    return next_pos

def game(players):
    print("{}, Welcome To Snakes And Ladders".format(" ".join(players)))
    input("Press Enter")
    while True:

        # Foreach player
        for player, current_pos in players.items():

            # Move player
            players[player] = move_player(player, current_pos)

            # Check win
            if players[player] > 100:
                return player

            # Next player
            input("Press Enter")


if __name__ == "__main__":
    players = setup_game()
    winner = game(players)
    print("Player {} won the game".format(winner))
