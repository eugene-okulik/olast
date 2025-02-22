def count_rez(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)  # использован метод pop чтобы получить значение и удалить его
        for _ in range(count):
            func(*args, **kwargs)
    return wrapper


@count_rez
def text_me(text):
    print(text)


text_me('text_in_func', count=5)

# Второй вариант

def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(count=3)
def text_me_2(text):
    print(text)


text_me_2('decorator_2')
