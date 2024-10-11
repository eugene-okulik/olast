import math

# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

leg_one = 3
leg_two = 4

hypotenuse = math.sqrt(leg_one**2 + leg_two**2)
square = 0.5 * leg_one * leg_two

print(f'Гипотенуза треугольника равна: {hypotenuse}, его площадь равна: {square}')
