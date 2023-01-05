import random as r
from math import fabs
win,lose,coins=0,0,30










# 1 : Guess the number
def guess_num():
    global lose,win,coins
    i = 1
    print("Welcome to the Guess the Number \n The rules are simple \n You guess a number(1-10) and if it matches with the random number the computer has chosen, You win!! \n You only get three tries though \n P.S. watch out for the temprature \n Hot is super close, Warm is close, Cold is far \nLets begin!!!")
    print("Please guess a number")
    target = r.randint(1,10)
    while i<4:
        guess = int(input())
        temp=fabs(target-guess)
        if guess != target:
            if temp<3:
                print(f"Hot!!")
            if 5>temp>=3:
                print(f"Warm")
            if temp>=5:
                print(f"Cold")
        if guess != target and i<3:
            print("Try again")
        if guess>10:
            print("Please select a number between 1 and 10")
        elif guess == target:
            print('You win')
            print()
            print()
            coins+=20
            win+=1
            break
        i+=1
    if i==4:
        print("You Lose!!")
        print(f"The number was {target}")
        print()
        print()
        lose+=1









# 2 : Hangman
def hangman():
    global win,lose,coins
    print("Welcome to the Hangman\n The rules are suuuuuuper complex \n .....Just kidding \n The 'Grammar Nazi' backstage thinks of a word and you have to guess it alphabet by alphabet or else there will be CONSEQUENCES!\n Dont worry though, you have 5 lives to get it right\n The Dashes represent the number of alphabets a word contains\n Enjoy!!")
    print()
    secret=['bulb', 'offset', 'referee', 'method', 'cheat', 'paradox', 'recommendation', 'enlarge', 'jelly', 'revise', 'year', 'emergency', 'abundant', 'pile', 'joy']
    word=r.choice(secret)
    guesses=""
    lives=5
    while lives>0:
        missing=0
        for i in word:
            if i in guesses:
                print(i,end="")
            else:
                print("- ",end="")
                missing+=1
        if missing==0:
            print("\nYou Win!!!")
            coins+=20
            win+=1
            break
        guess=input("\nGuess an Alphabet\n")
        guesses+=guess
        if guess not in word:
            lives-=1
            print(f"Nope.... \nTry again \nYou have {lives} lives remaining")
            if lives==4:
                print("Dont forget the Consequences!!!")
                print()
            if lives==3:
                print("|\n|\n|\n|\n|\n|")
                print()
            if lives==2:
                print("______")
                print("|\n|\n|\n|\n|\n|")
                print()
            if lives==1:
                print("______")
                print("|    |")
                print("|\n|\n|\n|\n|")
                print()
            if lives==0:
                print("______")
                print("|    |")
                print("|    O")
                print("|   /|\\")
                print("|   / \\")
                print("|_________")
                print("\\_________\\")
                print()
                print(f"\nYou lose!!\nThe word was {word}")
                lose+=1









# 3 : Stone Paper Scissors
def StnPprScr():
    global win,lose,coins
    playerwin=0
    playerlose=0
    turns=0
    print("Welcome to Stone Paper Scissors")
    print(" You know the rules\n Just type your pick and hope you win XD\n The best of 5 will win")
    print("Write stone paper or scissor")
    while turns<5:
        choices=["stone","paper","scissor"]
        hand=r.choice(choices)
        play=input("What do you choose?\n")
        if hand==play:
            print(f"Computer chose {hand}")
            print("draw")
        elif (hand=="scissor" and play=="paper") or (hand=="paper" and play=="stone") or (hand=="stone" and play=="scissor"):
            print(f"Computer chose {hand}")
            print("You lose")
            playerlose+=1
        elif (play=="scissor" and hand=="paper") or (play=="paper" and hand=="stone") or (play=="stone" and hand=="scissor"):
            print(f"Computer chose {hand}")
            print("You win!!!")
            playerwin+=1
        else:
            print("Not a valid input")
            playerlose+=1
        turns+=1
    if playerwin>playerlose:
        print("You beat the computer!!")
        coins+=20
        win+=1
    else:
        print("You could not beat the computer  :(")
        lose+=1



# 4 coin flip
def coinflip():

    print("This is a coinflipper ")

    print("The outcomes of the coinflipper can be heads or tails.")
    
    z="flip"
    x=input("Write flip if you want to flip the coin")
    y=x.lower()
    if y==z:
        choices=["Tails","Heads"]
        coin=r.choice(choices)
        if coin=="Heads":
            print("""
██╗      ██╗███████╗ █████╗ ██████╗ ███████╗
██║      ██║██╔════╝██╔══██╗██╔══██╗██╔════╝
███████║█████╗  ███████║██║  ██║███████╗
██╔══██║██╔══╝  ██╔══██║██║  ██║╚════██║
██║      ██║███████╗██║  ██║██████╔╝███████║
╚═╝      ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝
""")
        elif coin=="Tails":
            print("""  
​ ​​​████████╗ █████╗ ██╗██╗     ███████╗
​ ╚══██╔══╝██╔══██╗██║██║     ██╔════╝
​​​ ​   ​​██║   ███████║██║██║     ███████╗
​ ​   ██║   ██╔══██║██║██║     ╚════██║
​ ​   ██║   ██║  ██║██║███████╗███████║
​ ​   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝""")


# 5 diceroll
def diceroll():

    print("This is a diceroller ")

    print("The outcomes of the dice can be 1,2,3,4,5,6")
    
    z2="roll"
    x2=input("Write roll if you want to roll the dice")
    y2=x2.lower()
    if y2==z2:
        target = r.randint(1,6)
        if target==1:
            print("⚀")
        elif target==2:
            print("⚁")
        elif target==3:
            print("⚂")
        elif target==4:
            print("⚃")
        elif target==5:
            print("⚄")
        elif target==6:
            print("⚅")
            





#Game
def game():    
    global coins,win,lose
    player=input("Who is playing?\n")
    input(f"Welcome to the GameHub {player.title()}\nPress Enter to enter the 'Hub' \n")
    print("You will have 30 coins in the beggining\nEach game costs 10 coins to play\nWinnning gives you +20 coins while loosing takes away 10")
    print("1 : Guess the number\n2 : Hangman\n3 : Stone Paper Scissior\n4 : Coinflip\n5 : Diceroll")
    #Main loop
    while True:
        game=int(input("Please type the number corresponding to the game you want to play or 0 to quit: \n"))
        if coins==0:
            print("You are out of coins... Better luck next time.")
            break
        if game==0:
            print()
            print()
            print(f"You won {win} times and lost {lose} times")
            print("Thanks for playing! \nHave a nice day!!")
            break
        if game==1:
            print()
            print()
            coins-=10
            guess_num()
        if game==2:
            coins-=10
            print()
            print()
            hangman()
        if game==3:
            coins-=10
            print()
            print()
            StnPprScr()
            
        if game==4:
            print()
            print()
            coinflip()
        if game==5:
            print()
            print()
            diceroll()
        

        re=input(f"You have {coins} coins left\nWanna play more?(y/n)\n")
        if re == "y":
            print("1 : Guess the number\n2 : Hangman\n3 : Stone Paper Scissior\n4 : Coinflip\n5 : Diceroll")
            continue
        else:
            print()
            print()
            print(f"You won {win} times and lost {lose} times and you have {coins}")
            print("CREDITS\n")
            print("Thanks for playing! \nHave a nice day!!")
            break

#Play area
game()













