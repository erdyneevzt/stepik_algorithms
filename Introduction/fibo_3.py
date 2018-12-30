def fib_mod(n, m):

    # ----------- Ищем первый ноль в периоде
    fibo_list = [0, 1]

    # Начинаем с единицы
    i = 1

    while (fibo_list[i] % m) != 0:
        fibo_list.append(fibo_list[i-1] + fibo_list[i])
        i += 1
    # -------------

    # ------------- Проверка периодов 1,2,4
    period_nums = [1, 2, 4]

    for l in period_nums:
        # Докладываем числа в ряд в соответствии с периодом
        for j in range(i*l, i*l*2):
            fibo_list.append(fibo_list[j - 1] + fibo_list[j])

        ostatot_m = []
        # Получаем остаток от деления
        for j in range(len(fibo_list)):
            ostatot_m.append(fibo_list[j] % m)

        # Проверяем период
        if ostatot_m[1:i*l+1] == ostatot_m[i*l+1:i*l*2+1]:
            period = i*l
            break
    # print('Период равен=', period)
    # print('Остаток равен=', ostatot_m[n % period])
    return ostatot_m[n % period]
    # -----------------------------------


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()


# Решение валится на строке 9