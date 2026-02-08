numbers={4,22,43,17,36}
guesses=set()
fails=set()

print("Welcome to Secret Set")
print("Guess numbers from 1-50\n")

while guesses!=numbers:
    guess=int(input("Enter your guess: "))
    if guess in guesses:
        print("You've already guessed that correct!\n")
    elif guess in fails:
        print("You already guessed that wrong!\n")
    elif guess in numbers:
        print("You guessed correct!\n")
        guesses.add(guess)
    else:
        print("Wrong Guess!\n")
    
    print(guesses)

print("You guessed all the numbers!\n")

#HW:
#Unique Word Collector Game
#Player enters words; duplicates are ignored automatically.