#Guessing game

secret_word = "coconut"

i=1
guess = input("You have 3 tries to guess the secret word: ")

while i < 3 and guess != secret_word:
    print("Wrong guess, guess again :)")
    i += 1
    guess = input("Guess the secret word: ")

if guess == secret_word:
    i = 3
    print("Yay! you guessed correctly!")
else:
    print("Sorry, you lose")