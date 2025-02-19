def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()


def get_fibonacci_number(generator, n):
    for _ in range(n):
        result = next(generator)
    return result


fifth_number = get_fibonacci_number(fib_gen, 5)
fib_gen = fibonacci_generator()
two_hundredth_number = get_fibonacci_number(fib_gen, 200)
fib_gen = fibonacci_generator()
thousandth_number = get_fibonacci_number(fib_gen, 1000)
fib_gen = fibonacci_generator()
hundred_thousandth_number = get_fibonacci_number(fib_gen, 100000)

print("5-е число Фибоначчи:", fifth_number)
print("200-е число Фибоначчи:", two_hundredth_number)
print("1000-е число Фибоначчи:", thousandth_number)
print("100000-е число Фибоначчи:", hundred_thousandth_number)
