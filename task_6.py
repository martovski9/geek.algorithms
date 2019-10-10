import random


def main():
    # 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
    # 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
    # чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

    aim = random.randint(0, 100)
    looser = 1
    for i_try in range(10):
        n = int(input('Угадывай: '))
        if aim == n:
            print('Winner! ')
            looser = 0
            break
        else:
            if (aim > n):
                print('Я загадал бОльшее ')
            else:
                print('Я загадал мЕньшее ')
    if looser:
        print('Looser! ')
        print(aim)
    return 0


if __name__ == "__main__":
    main()
