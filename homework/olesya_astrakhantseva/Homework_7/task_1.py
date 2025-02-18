secret_number = 9

while True:
    user_input = int(input("Пожалуйста, введите свою цифру: "))
    if user_input == secret_number:
        print("Поздравляем, вы угадали!")
        break
    else:
        print("Не угадали, попробуйте еще раз :(")
