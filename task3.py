# random number
import random

random_number = random.randint(1,30)
print("Guess the number")
while True:
    my_guess = int(input("Enter your Guess"))
    if my_guess < random_number:
        print("Guessed the lower number")
    elif my_guess > random_number:
        print("Guessed the higher number")
    else:
        print("Guessed the correct number")
        break




# scramble the unscramble word
words = ['python','javascript','java','automation','pytest','selenium']


originalword = words[5]
scramble = originalword[ :: -1]

print("Unscramble this word:", scramble)

attempts = 7
for i in range(attempts):
    uservalue = input("Enter the word: ")

    if originalword.lower() == uservalue.lower():
        print("Player guess correct")
        break
    else:
        print("Player guess wrong")

else:
    print("Out of attempts!")
    print("The word is:", originalword)