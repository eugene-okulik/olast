temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

new_temperatures = list(filter(lambda x: x > 28, temperatures))
print('Отсортированный список температуры -', sorted(list(new_temperatures)))
print('Максимальная температура:', max(new_temperatures))
print('Минимальная температура:', min(new_temperatures))
print('Средняя температура:', round(sum(new_temperatures) / len(new_temperatures)))
