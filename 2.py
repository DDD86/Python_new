def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True  
    if number % 2 == 0:
        return False  

    limit = int(number**0.5) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False

    return True

LOWEST = 2
HIGHEST = 100000

while True:
    try:
        num = int(input(f"Введите число (от {LOWEST} до {HIGHEST}): "))
        if num < LOWEST or num > HIGHEST:
            print(f"Число должно быть от {LOWEST} до {HIGHEST}.")
            continue
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

if is_prime(num):
    print(f"{num} является простым числом.")
else:
    print(f"{num} является составным числом.")
