# name: Devan Clouse
# email: devan.clouse@gmail.com
# program: Rock Paper Scissors Game

# PUT YOUR CODE HERE

import random

x = 0

while x == 0:
    player = input("Enter your choice:\nR or r for rock\nP or p for paper\nS or s for scissors\nQ or q to quit\n")
    player = player.lower()

    if player == "r":
        player = "rock"
    if player == "p":
        player = "paper"
    if player == "s":
        player = "scissors"
    if player == "q":
        break

    computer = random.randrange(1, 4)

    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    elif computer == 3:
        computer = "scissors"

    print("Computer picked: ", computer)

    if player == computer:
        print("You tie against the computer\n")
    elif player == "rock":
        if computer == "paper":
            print("You lose against the computer\n")
        else:
            print("You win against the computer\n")
    elif player == "paper":
        if computer == "scissors":
            print("You lose against the computer\n")
        else:
            print("You win against the computer\n")
    elif player == "scissors":
        if computer == "rock":
            print("You lose against the computer\n")
        else:
            print("You win against the computer\n")

# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# R
# Computer picked:  paper
# You lose against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# P
# Computer picked:  scissors
# You lose against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# S
# Computer picked:  scissors
# You tie against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# r
# Computer picked:  paper
# You lose against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# r
# Computer picked:  scissors
# You win against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# r
# Computer picked:  rock
# You tie against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# p
# Computer picked:  paper
# You tie against the computer
#
# Enter your choice:
# R or r for rock
# P or p for paper
# S or s for scissors
# Q or q to quit
# Q