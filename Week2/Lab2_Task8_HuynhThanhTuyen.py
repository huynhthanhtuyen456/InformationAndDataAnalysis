import random

try_count = 5

if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter your integer: "))
            rand_number = random.randint(1, 10)

            if (try_count <= 0):
                print("You don't have any chances to try!")
                break

            if (number < rand_number or number > rand_number):
                print(f"Better luck next time! Let's try again. You have {try_count} times")
                try_count -= 1
                continue

            print(f"Your number {number} is a lucky number. You won the game!")
            break
        except ValueError:
            print("You typed an invalid integer! Please re-type a valid integer.\n")
