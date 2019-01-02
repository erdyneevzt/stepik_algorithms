# В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел,
# не превышающих 10^9, в порядке возрастания, во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk,
# не превышающих 10^9.
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.


a = list(map(int, input().split(" ")))[1:]
b = list(map(int, input().split(" ")))[1:]


def binary_search(a, b):
    l = 0
    r = len(a)-1
    while l <= r:
        m = l + (r - l)//2
        if a[m] == b:
            return m+1
        elif a[m] > b:
            r = m - 1
        else:
            l = m + 1
    return -1


for i in b:
    print(binary_search(a,i), end=' ')


# Решение из форума
# import bisect
#
# a = [int(x) for x in input().split()][1:]
# b = [int(x) for x in input().split()][1:]
#
# for x in b:
#     idx = bisect.bisect_left(a, x)
#     if idx == len(a) or a[idx] != x:
#         print(-1, end=" ")
#     else:
#         print(idx + 1, end=" ")
