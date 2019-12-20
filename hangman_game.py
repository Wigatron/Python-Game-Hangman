# Hangman Game


import time

name = input("What is you name? ")

print("Hello, " + name, "Time to play hangman!")
print("")

#wait timer for 1 second
time.sleep(1)

print("Start guessing....")
time.sleep(0.5)

#here we set the secret word
word = "secret"

#create a variable with an empty value
guesses = ""

#determine the number of turns
turns = 10

#create a while loop

#check if turns are more than zero

while turns > 0:
    failed = 0 #failed counter starts at zero
    for char in word: #for each character in secret_word
        if char in guesses: #see if the char is in the players guess
            print(char) #print out the char
        else:
            print("_")
            failed += 1 #if not found print a dash and increase the failed counter
    if failed == 0:
        print("You Won!!")
        break # exit the script

    print
    guess = input("guess a character:") #ask user to guess a char
    guesses += guess #set players guess to guesses
    if guess not in word: #if guess not in the secret word
        turns -= 1 #turnes counter decreases by 1
        print("Wrong") #print wrong
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Lose!!!")
