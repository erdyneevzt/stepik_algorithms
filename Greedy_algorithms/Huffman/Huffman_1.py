# По данной непустой строке s длины не более 104, состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k,
# встречающихся в строке, и размер получившейся закодированной строки.
# В следующих k строках запишите коды букв в формате "letter: code".
# В последней строке выведите закодированную строку.
# Sample Input 1:
#
# a
#
# Sample Output 1:
#
# 1 1
# a: 0
# 0
# Sample Input 2:
#
# abacabad
#
# Sample Output 2:
#
# 4 14
# a: 0
# b: 10
# c: 110
# d: 111
# 01001100100111

# string = str(input())
#
# freq_symb   = {}
# bin_dict    = {}
#
#
# # Cоздадим два словаря:
# # В первом будет символ: частота вхождения
# # Во втором будет сначала словарь с символами без значений, а в цикле они будут заполнены
# for i in set(string):
#     freq_symb[i] = [string.count(i)]
#     bin_dict[i] = ''
#
# n = len(freq_symb)
#
#
# for i in range(n-1):
#     # Сортируем значения от наименьшего значения внутри списка со значением. Смотри выше на [string.count(i)]
#     sorted_d = sorted(freq_symb.items(), key=lambda x: x[1][-1])
#     # Удаляем первые два узла которые будут объединены
#     del freq_symb[sorted_d[0][0]]
#     del freq_symb[sorted_d[1][0]]
#     # Создаем новый элемент, где ключом будет сложение символов:
#     # 'a'+'b' ='ab'
#     # Затем присваем ключу список:[Значение первого, Второго, Сумма].
#     # [0][1][-1] - Означает первый ключ, значение после ключа, последний элемент списка
#     freq_symb[sorted_d[0][0]+sorted_d[1][0]] = [sorted_d[0][1][-1], sorted_d[1][1][-1], sorted_d[0][1][-1]+sorted_d[1][1][-1]]
#     # Теперь добавляем двоичные символы в словарь bin_dict
#     # Берем оба предыдущих ключа, перебираем каждый символ в нем
#     # Младшее значение или левый элемент получают ноль в старший разряд
#     for j in sorted_d[0][0]:
#         bin_dict[j] = str(0) + bin_dict[j]
#     # Большее значение или правый элемент получают 1 в старший разряд
#     for j in sorted_d[1][0]:
#         bin_dict[j] = str(1) + bin_dict[j]
#
# # Особый случай для 1
# if len(bin_dict) == 1:
#     for key in bin_dict.keys():
#         bin_dict[key] = str(0)
#
# # Кодируем входное значение по словарю
# coded_str = ''
# for i in string:
#     coded_str += bin_dict[i]
#
# # Печатаем значения
# print(len(bin_dict), len(coded_str))
# for key, value in bin_dict.items():
#     print(key+':', value)
# print(coded_str)


import collections


def popmin(tree, codes, num):
    el = tree.pop(tree.index(min(tree)))
    for s in el[1]:
        codes[s] = num + codes[s]
    return el[0], el[1]


def main():
    sss = input().strip()
    count = collections.Counter(sss)
    print(count)
    codes = dict.fromkeys(count, '0' if len(count) == 1 else '')
    print(count)
    tree = [[count[key], key] for key in count]
    print(tree)
    while len(tree) > 1:
        val1, s1 = popmin(tree, codes, '0')
        val2, s2 = popmin(tree, codes, '1')
        tree.append([val1 + val2, s1 + s2])
    word = ''.join(codes[s] for s in sss)
    print(len(count), len(word))
    [print('{}: {}'.format(k, codes[k])) for k in sorted(codes)]
    print(word)


if __name__ == '__main__':
    main()