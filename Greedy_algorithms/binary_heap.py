# Первая строка входа содержит число операций 1≤n≤105.
# Каждая из последующих n строк задают операцию одного из следующих двух типов:
#
# Insert x, где 0≤x≤109 — целое число;
# ExtractMax.
#
# Первая операция добавляет число x в очередь с приоритетами,
# Вторая — извлекает максимальное число и выводит его.
# Sample Input:
#
# 6
# Insert 200
# Insert 10
# ExtractMax
# Insert 5
# Insert 500
# ExtractMax
# Sample Output:
#
# 200
# 500


# Строим структуру через binary max heap

# Количество операций
n_oper = int(input())

# Функция для добавления значения
def insert_val(tree, val):
    # Вставляем в конец значение
    tree.append(val)
    # Количество элементов в списке
    num_elem = len(tree)
    # Ставим указатель на последний добавленый индекс
    pointer     = num_elem-1
    # Перебираем звенья и меняем местами пока родитель не станет больше
    while tree[(pointer-1)//2] < tree[pointer] and pointer != 0:
        tree[(pointer-1)//2], tree[pointer] = tree[pointer], tree[(pointer-1)//2]
        pointer = (pointer-1)//2

# Просеивание вниз от старшего до младшего
def sift_down(tree):
    # Количество элементов в дереве
    num_elem = len(tree)
    i = 0
    # Альтернативный способ перебирающий все значения
    while 2*i+1 < num_elem:
        left = 2*i+1
        right = 2*i+2
        j = left
        if num_elem > right and tree[right] > tree[left]:
            j = right
        if tree[i] > tree[j]:
            break
        tree[i], tree[j] = tree[j], tree[i]
        i = j


def extract_max(tree):
    max_val = tree[0]
    tree[0] = tree[-1]
    tree.pop()
    sift_down(tree)
    return int(max_val)


# Список с деревьями
tree = []

i = 0

while i < n_oper:
    Oper_name = input()
    if Oper_name == 'ExtractMax':
        print(extract_max(tree))
    else:
        _ , val = Oper_name.split()
        insert_val(tree, int(val))
    i += 1



# Решение из форума

# class PriorityQueue(list):
#     @staticmethod
#     def _parent(i):
#         return (i + 1) // 2 - 1
#
#     @staticmethod
#     def _right_child(i):
#         return (i + 1) * 2
#
#     @staticmethod
#     def _left_child(i):
#         return (i + 1) * 2 - 1
#
#     def _safe_value(self, i):
#         try:
#             return self[i]
#         except IndexError:
#             return -float("inf")
#
#     def _swap(self, i, j):
#         self[i], self[j] = self[j], self[i]
#
#     def _next(self, i):
#         r_i = self._right_child(i)
#         l_i = self._left_child(i)
#         return r_i if self._safe_value(r_i) > self._safe_value(l_i) else l_i
#
#     def _last_idx(self):
#         return len(self) - 1
#
#     def _sift_up(self, n, i):
#         j = self._parent(i)
#         if j >= 0 and self[j] < n:
#             self._swap(i, j)
#             self._sift_up(n, j)
#
#     def _sift_down(self, n, i):
#         j = self._next(i)
#         if j <= self._last_idx() and self[j] > n:
#             self._swap(i, j)
#             self._sift_down(n, j)
#
#     def append(self, n):
#         super().append(n)
#         self._sift_up(n, self._last_idx())
#
#     def extract_max(self):
#         self._swap(0, self._last_idx())
#         _max = self.pop()
#         if len(self) > 0:
#             self._sift_down(self[0], 0)
#         return _max
#
#
# def main():
#     total = int(input())
#     pq = PriorityQueue()
#     for i in range(total):
#         command = input()
#         if command.startswith('Insert'):
#             _, n = command.split()
#             pq.append(int(n))
#         elif command.startswith('ExtractMax'):
#             print(pq.extract_max())
#
#
# if __name__ == '__main__':
#     main()