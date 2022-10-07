player1 = str(input("enter the player name 1:"))
player2 = str(input("enter the player name 2:"))
choice1 = str(input("enter the choice 1 between rock,paper,scissors:"))
choice2 = str(input("enter the choice 2 between rock,paper,scissors:"))
if choice1 == choice2:
    print(player1,"and",player2,"are tie")
elif choice1 == "rock":
    if choice2 == "scissors":
        print(player1,"puts",choice1,"and",player2,"puts",choice2,"and",player1,"wins!",player2,"loses!")
    else:
        print(player1,"puts",choice1,"and",player2,"puts",choice2,"and",player2,"wins!",player1,"loses!")
elif choice1 == "paper":
    if choice2 == "rock":
        print(player1,"puts",choice1,"and",player2,"puts",choice2,"and",player1,"wins!",player2,"loses!")
    else:
        print(player1,"puts",choice1,"and",player2,"puts",choice2,"and",player2,"wins!",player1,"loses!")
elif choice1 == "scissors":
    if choice2 == "paper":
        print(player1,"puts",choice1,"and",player2,"puts",choice2,"and",player1,"wins!",player2,"loses!")
    else:
        print(player1,"puts",choice1,"and",player2,"puts",choice2,"and",player2,"wins!",player1,"loses!")
