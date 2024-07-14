def to_hex(number):
    if number == 0:
        return '0'
    
    hex_digits = "0123456789ABCDEF"
    hex_str = ''
    
    while number > 0:
        remainder = number % 16
        hex_str = hex_digits[remainder] + hex_str
        number //= 16
    
    return hex_str

try:
    number = int(input("Введите целое число: "))
    print("Результат функции hex:", hex(number))
    custom_hex = to_hex(number)
    print("Результат пользовательской функции:", custom_hex)
except ValueError:
    print("Пожалуйста, введите целое число.")
