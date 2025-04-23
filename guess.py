import random

print("Привет! Я загадал число от 1 до 100. Попробуй угадать!")

secret_number = random.randint(1, 100)
attempts = 0

level = input("Выбери уровень сложности: легкий / средний / сложный: ").lower()

if level == "легкий":
    max_number = 50
elif level == "средний":
    max_number = 100
else:
    max_number = 200

secret_number = random.randint(1, max_number)

while True:
    guess = input("Твой вариант: ")

    if not guess.isdigit():
        print("Пожалуйста, введи число.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Слишком мало!")
    elif guess > secret_number:
        print("Слишком много!")
    else:
        print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток.")
        break
