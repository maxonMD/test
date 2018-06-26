import random


def userguess():
    userguess = input("Enter R for rock, P for paper, or S for scissors: ").lower()

    if userguess == 's':
        print("you have selected scissors")
        return userguess
    elif userguess == 'r':
        print("you have selected rock")
        return userguess
    elif userguess == 'p':
        print("you have selected paper")
        return userguess

def computerguess():
    compguess = random.choice(['r', 'p', 's'])

    if compguess == "r":
        print("the computer selected rock")
        return compguess
    elif compguess == 'p':
        print("the computer selected paper")
        return compguess
    elif compguess == 's':
        print("the computer selected scissors")
        return compguess

def game():
    while True:
        user = userguess()
        comp = computerguess()

        if comp == user:
            print("tie try again")
            game()
        elif comp == 'r' and user == 'p':
            print("You win")
        elif comp == 'r' and user == 's':
            print("You lose")
        elif comp == 'p' and user == 's':
            print("You lose")
        elif comp == 'p' and user == 'r':
            print("You win")
        elif comp == 's' and user == 'p':
            print("You win")
        elif comp == 'p' and user == 's':
            print("You lose")


game()