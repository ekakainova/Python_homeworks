import math


def square(a):
    return math.ceil(a * a)


side = float(input("Сторона квадрата равна: "))
print(f"Площадь квадрата равна: {square(side)}")
