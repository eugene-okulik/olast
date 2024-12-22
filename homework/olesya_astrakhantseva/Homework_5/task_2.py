result_1 = 'результат операции: 42'
result_2 = 'результат операции: 514'
result_3 = 'результат работы программы: 9'

for result in result_1, result_2, result_3:
    number = int(result[result.index(':') + 1:].strip())
    print(number + 10)
