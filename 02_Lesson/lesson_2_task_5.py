def month_to_season(m):
    if m == 1 or m == 2 or m == 12:
        return ("Зима")
    elif 3 <= m <= 5:
        return ("Весна")
    elif 6 <= m <= 8:
        return ("Лето")
    elif 9 <= m <= 11:
        return ("Осень")
    else:
        return ("Такого месяца нет")


try:
    month = int(input("Введите номер месяца от 1 до 12: "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12")
