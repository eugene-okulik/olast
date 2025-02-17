stroki = [
    'result_1 = результат операции: 42',
    'result_2 = результат операции: 514',
    'result_3 = результат работы программы: 9'
]


def result(stroki):
    for stroka in stroki:
        number = int(stroka.split()[-1])
        print(number + 10)


result(stroki)