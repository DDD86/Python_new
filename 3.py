from random import randint

LOWER = 0
UPPER = 1000
COUNTER = 10

number = randint(LOWER, UPPER)
print(f"Загадано число от {LOWER} до {UPPER}. Угадайте его за {COUNTER} попыток.")

for attempt in range(1, COUNTER + 1):
    try:
        guess = int(input(f"Попытка {attempt}: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if guess == number:
        print("Поздравляем! Вы угадали число!")
        break
    elif guess > number:
        print("Меньше")
    else:
        print("Больше")

    if attempt == COUNTER:
        print(f"Вы исчерпали все попытки. Загаданное число было: {number}")
