import sys

sys.set_int_max_str_digits(1000000)
#
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
#
# print(fibonacci(112121))  # Output: 8


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(11))