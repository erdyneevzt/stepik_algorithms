# ------------------------- Небольшое число Фибоначии -------------------------
# Дано целое число 1≤n≤40, необходимо вычислить n-е число Фибоначчи (напомним, что F0=0, F1=1 и Fn=Fn−1+Fn−2
# при n≥2).

# Sample Input:
# 3
# Sample Output:
# 2


def fib(n):
    # put your code here
    if n <= 1:
        return n
    else:
        fibo_list = [0,1]
        for i in range(n):
            fibo_list.append(fibo_list[i]+fibo_list[i+1])
        return fibo_list[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()


# Решение из форума:
# def fib(num):
#
#     prev, cur = 0, 1
#
#     for i in range(1, num):
#         prev, cur = cur, prev + cur
#
#     return cur