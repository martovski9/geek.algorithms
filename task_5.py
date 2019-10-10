def main():
    # 45. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
    # включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

    i_sym = 32
    i_line = 1

    while 1:
        for i_line in range(11):
            if i_sym < 128:
                print(i_sym, '-', chr(i_sym), end=' ')
                i_sym += 1
                i_line += 1
            else:
                return 127
            i_line += 1
        print('\n')

    return 0


if __name__ == "__main__":
    main()
