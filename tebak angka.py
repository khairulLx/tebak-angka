import random

rahasia = random.randint(1, 100)
print("=" * 40)
print("Number Guessing Game")
print("=" * 40)

print("1. Easy Level")
print("2. Medium Level")
print("3. Hard Level")
level = int(input("Choose a level: "))

batas = 0
if level == 1:
    batas = 20
elif level == 2:
    batas = 15
elif level == 3:
    batas = 10

for percobaan in range(batas):
    jawaban = int(input(f"Attempt {percobaan + 1}, enter your guess: "))
    if jawaban == rahasia:
        print("Congratulations! Your answer is correct!!!")
        break
    else:
        if jawaban < rahasia:
            print("Your guess is too small")
        else:
            print("Your guess is too big")

else:
    print("Oops! You've run out of chances")

print("The secret number was:", rahasia)
