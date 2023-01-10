# GUESS THE NUMBER GAME
import random
def Guess_Number(a,b,actual):
    guess=int(input(f"Enter a number between {a} and {b} \n"))
    nguess=1
    while guess!=actual:
        if guess>actual:
            guess=int(input(f"Enter the smaller number\n"))
            nguess+=1
        else:
            guess = int(input(f"Enter the bigger number\n"))
            nguess+=1
    print(f"You have guessed the number in {nguess} guesses")
    return nguess

if __name__ == '__main__':
    a=int(input("Enter the value of a\n"))
    b=int(input("Enter the value of b\n"))
    print("First player turn\n ")
    actual1=random.randint(a,b)
    g1=Guess_Number(a,b,actual1)
    print("Second player turn ")
    actual2=random.randint(a,b)
    g2=Guess_Number(a,b,actual2)

    if g1>g2 :
        print("Second player wins the game\n ")
    elif g1<g2:
        print("First player wins the game\n")

    else :
        print("It is a tie situation\n")

    print(f"First player guess number {g1} and the second player guess number {g2}")
