# В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой,
# соответственно. Следующие n строк содержат по два целых числа ai и bi (ai≤bi) — координаты концов отрезков.
#  Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 108 по модулю.
#  Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки
# в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
#
#
# Sample Input:
#
# 2 3
# 0 5
# 7 10
# 1 6 11
# Sample Output:
#
# 1 0 0
#
from bisect import bisect, bisect_left

n, m = map(int, input().split(" "))

left_ls    = []
right_ls   = []

for i in range(n):
    left, right = map(int, input().split(" "))
    left_ls.append(left)
    right_ls.append(right)

points = list(map(int, input().split(" ")))


def fast_sort(ls):
    if ls == []:
        return []
    else:
        m       = ls[0]
        left    = fast_sort([x for x in ls[1:] if x < m])
        right   = fast_sort([x for x in ls[1:] if x >= m])
        return left + [m] + right

# Отсортированные списки
# Такой способ неподходит (Слишком долго):
# Либо нужно разбивать списки на три
# Либо выбирать случайный опорный элемент
# left_ls     = fast_sort(left_ls)
# right_ls    = fast_sort(right_ls)
left_ls.sort()
right_ls.sort()

all_answers = []
for i in range(m):
    all_answers.append(bisect(left_ls,  points[i]) - bisect_left(right_ls, points[i]))

print(*all_answers, sep=' ')


# Решение из форума
# n, m = [int(x) for x in input().split()]
#
# a = []
# for i in range(0, n):
#     l, r = [int(x) for x in input().split()]
#     a.append([l, -1])
#     a.append([r, 1])
#
# p = [int(x) for x in input().split()]
# for i in range(m):
#     a.append([p[i], 0, i])
#
#
# a.sort()
# res = [0] * m
# #print(a)
# curr = 0
# pi = 0
# for i in range(len(a)):
#     if a[i][1] == 1:
#         curr += -1
#     if a[i][1] == -1:
#         curr -= -1
#     if a[i][1] == 0:
#         res[a[i][2]] = curr
#
# print(*res)