import random

def end(amount):
    if amount <= 0:
        print("You are out of money")
        exit()
    if amount > 0:
        while True:
            try:
                play = int(input("Enter 1 to continue or 0 to quit"))
                if play == 1:
                    break
                elif play == 0:
                    exit()
            except ValueError:
                print("Please enter 1 to play or 0 to quit")
                continue

def determinewinnings(bet, c, total, amount):
    if c == 'h' and total >= 8:
        print("You have won " + str(bet))
        return amount + bet
    elif c == 'l' and total <= 6:
        print("You have won " + str(bet))
        return amount + bet
    elif c == 's' and total == 7:
        print("You have won " + str(bet * 4))
        return amount + bet * 4
    else:
        print("You have lost " + str(bet))
        return amount - bet

def getroll():
    rolla = random.randint(1, 6)
    return rolla

def getbet(amount):
    while True:
        try:
            print("You now have $" + str(amount) + " dollars")
            bet = int(input("Place your bet "))
            if bet < 0 or bet > amount:
                print("Insufficient funds: try something smaller ")
                continue
            elif bet == 0:
                print("goodbye")
                exit(0)
            elif bet > 0 or bet <= amount:
                return bet
        except ValueError:
            print("please enter a valid number")

def gethighlow():
    while True:
        try:
            c = input("Enter H for high, S for sevens and L for low: ").lower()
            if c == "s" or c == "h" or c == "l":
                if c == "h":
                    print("You bet high")
                    return c
                elif c == "l":
                    print("You bet low")
                    return c
                elif c == "s":
                    print("You bet sevens")
                return c
            else:
                print("Enter a valid option")
        except ValueError:
            print("You have entered in an invalid character ")

def game():
    amount = 100
    while True:
            bet = getbet(amount)
            c = gethighlow()
            print("You have " + str(amount) + " dollars")
            roll1 = getroll()
            roll2 = getroll()
            total = (roll1 + roll2)
            print("Dice 1 = " + str(roll1))
            print("Dice 2 = " + str(roll2))
            print("The total of your roll is " + str(total))
            amount = determinewinnings(bet, c, total, amount)
            print("You now have " + str(amount) + " dollars")
            end(amount)

game()