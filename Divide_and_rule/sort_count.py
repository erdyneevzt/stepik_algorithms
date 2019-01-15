# Задача на программирование: сортировка подсчётом
#
#
# Первая строка содержит число 1≤n≤104, вторая — n натуральных чисел,
# не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.
#
#
# Sample Input:
#
# 5
# 2 3 9 2 9
# Sample Output:
#
# 2 2 3 9 9

len_list = int(input())
num_list = [int(i) for i in input().split()]

def count_sort(ls, n):
    zero_list = [0] * 10
    for i in range(n):
        zero_list[ls[i]-1] = zero_list[ls[i]-1] + 1
    pos = 0
    for i in range(10):
        for j in range(zero_list[i]):
            ls[pos] = i+1
            pos     = pos + 1

count_sort(num_list, len_list)
print(' '.join(str(i) for i in num_list))

# Решение из форума
# n = int(input())
# data = [int(i) for i in input().split()]
# count = [(" " + str(i)) * data.count(i) for i in range(11) if data.count(i) > 0]
# print("".join(count).strip())