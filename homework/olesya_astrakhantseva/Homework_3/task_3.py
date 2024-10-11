import math

# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

number_one = 30
number_two = 50

result_arithmetic_mean = (number_one + number_two) / 2
result_geometric_mean = math.sqrt(number_one * number_two)

print(f'Среднее арифметическое чисел равно: {result_arithmetic_mean}, среднее геометрическое равно:'
      f' {result_geometric_mean}')
