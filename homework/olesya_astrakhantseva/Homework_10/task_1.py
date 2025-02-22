def generator(func):
    def wrapper():
        result = func()
        print('Finished')
        return result
    return wrapper


@generator
def greeting():
    print('Привет, друг, тут функция')


@generator
def say_hi():
    print('Hi')

greeting()
say_hi()
