# Число инверсий
# Про инверсии: https://ru.stackoverflow.com/questions/375825/%D0%A0%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D1%8F%D0%B9-%D0%B8-%D0%B2%D0%BB%D0%B0%D1%81%D1%82%D0%B2%D1%83%D0%B9-%D0%BF%D0%BE%D0%B4%D1%81%D1%87%D0%B5%D1%82-%D0%BA%D0%BE%D0%BB%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%B0-%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B9-%D0%B2-%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2%D0%B5/375841#375841
#
# Первая строка содержит число 1≤n≤105, вторая — массив A[1…n], содержащий натуральные числа,
# не превосходящие 109. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
# (Такая пара элементов называется инверсией массива. Количество инверсий в массиве является
# в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве
# инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

def merge_sort(ls):
    inv_num = 0
    if len(ls) > 1:
        # Индекс центра списка
        m = len(ls)//2
        left_elem   = ls[:m]
        right_elem  = ls[m:]

        inv_num += merge_sort(left_elem)
        inv_num += merge_sort(right_elem)

        # Указатели
        i, j, k = 0, 0, 0
        while i < len(left_elem) and j < len(right_elem):
            if left_elem[i] <= right_elem[j]:
                ls[k]   = left_elem[i]
                i       += 1
            else:
                ls[k]   = right_elem[j]
                j       += 1
                inv_num += len(left_elem) - i
            k += 1


        while i < len(left_elem):
            ls[k]   = left_elem[i]
            i       += 1
            k       += 1

        while j < len(right_elem):
            ls[k]   = right_elem[j]
            j       += 1
            k       += 1

    return inv_num



if __name__ == "__main__":
    n = int(input())
    ls = list(map(int, input().split(" ")))
    inv_num = merge_sort(ls)
    print(inv_num)
    # print(ls)


# Решение из форума
# def merge(a, b):
#     tmp = []
#     global k
#     while a and b:
#         if a[0] <= b[0]:
#             tmp.append(a.pop(0))
#         else:
#             tmp.append(b.pop(0))
#             k += len(a)
#     tmp.extend(a or b)
#     return tmp
#
#
# def mergesort(lst):
#     if len(lst) == 1:
#         return lst
#     m = len(lst) // 2
#     return merge(mergesort(lst[: m]), mergesort(lst[m:]))
#
#
# def main():
#     n = int(input())
#     queue = [int(i) for i in input().split()]
#     mergesort(queue)
#     print(k)
#
#
# if __name__ == '__main__':
#     k = 0
#     main()