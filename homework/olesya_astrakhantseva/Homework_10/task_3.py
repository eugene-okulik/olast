def result(func):
    def wrapper(first, second, *args, **kwargs):
        global operation
        if first < 0 or second < 0:  # Проверяем умножение первым
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@result
def culc(first, second, operator):
    if operator == "+":
        return first + second
    elif operator == "-":
        return first - second
    elif operator == "*":
        return first * second
    elif operator == '/':
        if second != 0:  # Проверка на деление на ноль
            return first / second


num1, num2 = map(int, input("Введите два числа : ").split())

print(culc(num1, num2))
