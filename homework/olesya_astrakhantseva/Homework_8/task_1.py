import random

salary = int(input("Введите вашу зарплату: "))

bonus = random.choice([True, False])

def result_salary(zarplata, bonus_rez):
    if bonus_rez:
        bonus_amount = random.randint(1000, 5000)
        total_salary = zarplata + bonus_amount
    else:
        total_salary = zarplata
    return f"${total_salary}"

final_result = result_salary(salary, bonus)
print(f"{salary}, {bonus} - {final_result}")