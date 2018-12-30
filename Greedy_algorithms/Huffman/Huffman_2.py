# Декодер Хаффмана
# Обратная задача Huffman_1
# Что плохо в алгоритме
# Перебираются все значения хотя нужно идти по дереву
# Вместо этого ищу все и беру с минимальной длиной вхождения


# n_dict, str_len = (int(i) for i in input().split())
#
# dict_name = {}
# for i in range(n_dict):
#     sym, val = input().split()
#     # Двоеточие нам не нужно поэтому берем только первый символ
#     dict_name[sym[0]] = val
#
# # То что декодируем
# coded_str = input()
#
# i = 0
# temp_dict = {}
# answer = ''
# while i < str_len:
#     # Перебираем все ключи и значения в словаре
#     for key, value in dict_name.items():
#         # Если начало совпадает добавляем во временный список
#         if coded_str.startswith(value):
#             temp_dict[key] = value
#     # Берем символ с минимальным значением
#     sym_to_add = min(temp_dict, key=temp_dict.get)
#     # Добавляем к ответу
#     answer  += sym_to_add
#     # Обнуляем словарь
#     temp_dict  = {}
#     # Меняем счетчик
#     i          += len(dict_name[sym_to_add])
#     # Срезаем начало входной последовательности
#     coded_str  = coded_str[len(dict_name[sym_to_add]):]
#
#
# print(answer)



# Еще одно решение из форума

def decode(dictionary, encoded_string):
    sequence = ''
    decoded_string = ''
    for symbol in encoded_string:
        sequence += symbol
        if sequence in dictionary:
            decoded_string += dictionary[sequence]
            sequence = ''
    return decoded_string


def main():
    k, l = map(int, input().split())
    dictionary = {}
    for i in range(k):
        data = input().split(': ')
        dictionary[data[1]] = data[0]
    encoded_string = input()
    print(decode(dictionary, encoded_string))


if __name__ == "__main__":
    main()