def fib_mod(n, m):
    pisano = []
    pisano.append(0)

    # при делении на 1 остаток будет всегда 0
    if m == 1:
        return pisano

    pisano.append(1)

    # при m > 0 остатки от деления первого и второго числа Фибоначчи
    # всегда 0 и 1
    if n <= 1:
        return pisano

    n0 = 0
    n1 = 1
    for __ in range(m * 6):
        # для ускорения вычисляем полностью числа Фибоначчи
        # берём только остатки по модулю m
        n0, n1 = n1, (n0 + n1) % m

        pisano.append(n1 % m)

        # Проверяем не начался ли новый период
        # период всегда начинается с 0 и 1
        if pisano[len(pisano) - 1] == 1 and pisano[len(pisano) - 2] == 0:
            break

    return pisano[:-2]
    # -----------------------------------


def main():
    n, m = map(int, input().split())
    pisano = fib_mod(n, m)
    print(pisano[n % len(pisano)])

if __name__ == "__main__":
    main()


# Решение из форума
# n,m=map(int,input().split())
# o,i=[0,1],2
# while not (o[i-2]==0 and o[i-1]==1) or i<=2:
# 	o.append((o[i-2]+o[i-1])%m)
# 	i+=1
# print(o[n%(i-2)])