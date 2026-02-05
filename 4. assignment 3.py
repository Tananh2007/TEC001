from random import randint
print("Welcome")
print("I have chosen a number from 1 to 10. Let try")
ans = randint(1, 10)
while True:
     userAns = int(input("Enter a number: "))
     if userAns == ans:
        print("You guessed right")
        break
     elif userAns < ans:
        print("You guessed too low")
     else:
        print("You guessed too high")
