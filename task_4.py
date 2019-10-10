# coding utf-8



def my_series(n):
    if n==1:
        return 1
    else:
        return my_series(n-1)/-2


def main():
    # 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n)
    # вводится с клавиатуры.
    i=1
    n=0
    res=0.0
    while n <= 0:
        n = int(input('Введите число элементов ряда: '))
    while i<=n:
        res += my_series(i)
        i+=1

    print ('Сумма нашего ряда: ', res)

    return 0


if __name__ == "__main__":
        main()
