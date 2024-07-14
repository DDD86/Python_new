def triangle_type(a, b, c):
    if a == b and b == c:
        return "Равносторонний треугольник"
    elif a == b or b == c or a == c:
        return "Равнобедренный треугольник"
    else:
        return "Разносторонний треугольник"

def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return triangle_type(a, b, c)
    else:
        return "Треугольника с такими сторонами не существует!"


a, b, c = map(int, input("Введите три стороны треугольника: ").split())
print(is_triangle(a, b, c))
