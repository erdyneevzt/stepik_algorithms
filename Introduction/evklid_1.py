# По данным двум числам 1≤a,b≤ 2⋅10**9 найдите их наибольший общий делитель.

# def gcd(a, b):
#     if a != 0 and b !=0:
#         if a > b:
#             a = a % b
#             return gcd(a,b)
#         else:
#             b = b % a
#             return gcd(a,b)
#     else:
#         if a == 0:
#             return b
#         else:
#             return a

# Решение из форума
def gcd(a, b):
    return gcd(b, a % b) if b else a

# Более читаемый вариант
# def gcd(a, b):
#     if b == 0:
#         return a
#
#     return gcd(b, a % b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()

