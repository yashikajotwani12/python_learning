import random
randnumber=random.randint(1,100)
print(randnumber)
userGuess=None
guesses=0
while(userGuess!=randnumber):
    userGuess=int(input("Enter Your Guess:"))
    if(userGuess==randnumber):
       print("You Guessed It right!!")
    else:
       print("you Guessed it wrong!!")
       
