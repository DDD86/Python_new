def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Введите количество чисел Фибоначчи: "))
fibonacci_gen = fibonacci_generator()  # Создаем экземпляр генератора

fibonacci_numbers = [next(fibonacci_gen) for _ in range(n)]
print(f"Fibonacci numbers: {fibonacci_numbers}")
