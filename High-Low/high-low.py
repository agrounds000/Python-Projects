from random import randint

def getRandomNumber() :
    randomNum = randint(1, 100)
    return randomNum

random = getRandomNumber()

running = True

playerGuess = ""

print ("Guess a random number between 1 and 100!")

while playerGuess != random :
    playerGuess = int(input(""))
    if playerGuess > random :
        print ("Too high...")
        continue
    elif playerGuess < random :
        print ("Too low...")
        continue
    elif playerGuess == random :
       playAgain = input("You win!! Play again (yes) (no)?")
       if playAgain == "yes" :
           print ("Guess a new number between 1 and 100!")
           random = getRandomNumber()
           continue
        elif playAgain == "no" :
            print ("Okay, bye!")
            break
        else :
            print ("Invalid input? Shutting down!")
            return;
      
        
    
