import random

def end(den):
    try:
        inscanner = int(input("Place your bet. Enter 0 to quit: "))
        if inscanner == 0:
            print("You have exited goodbye")
            exit()
    except ValueError:
        print("nothing")
        end(den)

def determinewinnings(bet, c, total, amount):
    if c == 'H' and total >= 8:
        print("You have won " + str(bet))
        return bet
    elif c == 'L' and total <= 6:
        print("You have won " + str(bet))
        return bet
    elif c == 'S' and total == 7:
        print("You have won " + str(bet*4))
        return bet*4
    else:
        print("You have lost " + str(bet))
        return amount - bet

def getroll():
    rolla = random.randint(1, 6)
    return rolla

def getbet(amount, bet):
    #bet = int(input("Place your bet "))
   #while True:
    try:
        if bet < 0 or bet > amount:
            print("Please enter a reasonable bet")
        elif bet == 0:
            print("goodbye")
            exit(0)
        elif bet < 0 or bet > amount:
            return bet
        #break
    except ValueError:
        print("please enter a valid number")

def gethighlow(c):
    #c = input("Enter H for high, S for sevens and L for low: ").lower()
    if c == "s" or c == "h" or c == "l":
        return c
    else:
        print("You have entered in an invalid character")

"""def game2(amount):
    while getbet(amount) != 0 and amount > 0:
        roll1 = getroll()
        roll2 = getroll()
        total = (roll1 + roll2)
        print("Dice 1 = " + str(roll1))
        print("Dice 2 = " + str(roll2))
        print("You rolled a " + str(total))
        if gethighlow() == "h":
            print("You bet high")
        elif gethighlow() == "l":
            print("You bet low")
        elif gethighlow() == "s":
            print("You bet sevens")
        amount = determinewinnings(bet, c, total, amount)
        print("You now have $ " + str(amount) + " dollars")
        end(den)
        break"""
def game():
    while True:
        try:
            amount = 100
            bet = int(input("Place your bet "))
            c = input("Enter H for high, S for sevens and L for low: ").lower()
            while True:
                if amount <= 0:
                    print("You are out of money please go get some more")
                    exit(0)
                try:
                    print("You have " + str(amount) + " dollars")
                    getbet(amount, bet)
                    den = False
                    while not den:
                        gethighlow(c)
                        while getbet(amount, bet) != 0 and amount > 0 :
                            roll1 = getroll()
                            roll2 = getroll()
                            total = (roll1 + roll2)
                            print("Dice 1 = " + str(roll1))
                            print("Dice 2 = " + str(roll2))
                            print("Therefore you rolled a " + str(total))
                            if gethighlow(c) == "h":
                                print("You bet high")
                            elif gethighlow(c) == "l":
                                print("You bet low")
                            elif gethighlow(c) == "s":
                                print("You bet sevens")
                            amount = determinewinnings(bet, c, total, amount)
                            print("You now have $" + str(amount) + " dollars")
                            end(den)
                            den = True
                            break
                except ValueError:
                    print("Please place a bet based on your remaining funds")
                    continue
        except ValueError:
            print("please enter a valid item")

game()