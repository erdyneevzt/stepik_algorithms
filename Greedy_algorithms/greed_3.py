# По данному числу 1≤n≤109 найдите максимальное число k,
# для которого n можно представить как сумму k различных натуральных слагаемых.
# Выведите в первой строке число k, во второй — k слагаемых.
#
# Sample Input 1:
# 4
# Sample Output 1:
# 2
# 1 3
# Sample Input 2:
# 6
# Sample Output 2:
# 3
# 1 2 3
#


n = int(input())

ls = []

i = 1
while 1:
    if n - i == 0:
        ls.append(i)
        break
    elif n / i > 2:
        n -= i
        ls.append(i)
    i += 1

print(len(ls))
for i in ls:
    print(i, end = ' ')


# Альтернативное решение из форума
# n = int(input())
# i = 1
# numbers = []
# while n > 2*i:
#     n -= i
#     numbers.append(i)
#     i += 1
#
# numbers.append(n)
# print(i)
# print(*numbers, sep=' ')

