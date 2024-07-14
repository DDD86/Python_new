from fractions import Fraction

def parse_fraction(fraction_str):
    numerator, denominator = map(int, fraction_str.split('/'))
    return Fraction(numerator, denominator)

try:
    fraction1_str = input("Введите первую дробь (в формате a/b): ")
    fraction2_str = input("Введите вторую дробь (в формате a/b): ")

    fraction1 = parse_fraction(fraction1_str)
    fraction2 = parse_fraction(fraction2_str)

    sum_fractions = fraction1 + fraction2
    product_fractions = fraction1 * fraction2

    print(f"Сумма дробей: {sum_fractions}")
    print(f"Произведение дробей: {product_fractions}")
except ValueError:
    print("Пожалуйста, введите дроби в правильном формате (a/b).")
