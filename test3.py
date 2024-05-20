"""
Вам необходимо разработать алгоритм на языке программирования Python, который будет выполнять следующую задачу:
Дан список из целых чисел. Вам нужно найти и вернуть сумму двух наименьших значений из этого списка.
Нельзя использовать встроенные функции Python.

Функция должна иметь следующую сигнатуру:
def find_sum_of_two_smallest_numbers(numbers: List[int]) -> int:

Примеры:
1. Если на вход подаются следующие числа: [5, 2, 8, 1, 9], то функция должна вернуть 3 (1 + 2 = 3).
2. Если на вход подаются следующие числа: [10, 4, 5, 8, 9], то функция должна вернуть 9 (4 + 5 = 9).
У вас есть неограниченное количество попыток и нет ограничения по времени выполнения. Проверьте свое решение на различных тестовых данных.
"""

from typing import List
import time


def find_sum_two_smallest_numbers(numbers: List[int]) -> int:
    first_smallest_number = float("inf")
    second_smallest_number = float("inf")

    for num in numbers:
        if num < first_smallest_number:
            second_smallest_number = first_smallest_number
            first_smallest_number = num
        elif num < second_smallest_number:
            second_smallest_number = num

    return first_smallest_number + second_smallest_number


print(find_sum_two_smallest_numbers([5, 2, 8, 1, 9]))
print(find_sum_two_smallest_numbers([10, 4, 5, 8, 9]))
