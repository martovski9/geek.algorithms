# coding: utf-8

# привычнее работать с основной и дополнительными функциями. Субъективно.
def main():
    # Урок 1.Задание 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
    n = 0
    while (n < 100) or (n > 999):
        n = int(input("Введи трехзначное число: "))
    h = int(n / 100)
    d = n % (h * 100)
    d1 = int(d / 10)
    # здесь может случиться делениие на 0, проверим
    if d1:
        u = d % (d1 * 10)
    else:
        #при второй цифре 0 (101, 109) в остаток деления на сотни сразу попадают едиинцы
        u = d
    print("сумма цифр введнного числа: ", h + d1 + u, "\nпроизведение цифр введенного числа: ", h * d1 * u)

    # Урок 1.Задание 2.
    # Урок 1.Задание 3.
    # Урок 1.Задание 4.
    return 0


if __name__ == "__main__":
    main()
