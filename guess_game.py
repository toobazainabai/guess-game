import random

attempts=5
# computer will choose the number randomly between 1 to 50
choosen_num=random.randint(1, 50)

for i in range (attempts):
    guess_num=int(input("Enter your guess number between 1 to 50: "))
    if guess_num==choosen_num:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("sorry your guess is wrong.please try again.")

else:
    print("You've used all your attempts. Better luck next time!")
print(f"The correct number was: {choosen_num}")

