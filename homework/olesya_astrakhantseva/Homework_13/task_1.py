import os
import datetime

my_path = os.path.dirname(__file__)
path_to_homework = os.path.dirname(os.path.dirname(my_path))
path_to_eugene = os.path.join(path_to_homework, 'eugene_okulik',
                              'hw_13', 'data.txt')


def read_file():
    with open(path_to_eugene, 'r', encoding='utf-8') as new_file:
        for line in new_file:
            yield line


date_list = []
for data_line in read_file():
    date_str = data_line[3:29]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    date_list.append(date)

print(date_list[0] + datetime.timedelta(days=7))
print(date_list[1].strftime('%A'))
delta = datetime.datetime.now() - date_list[2]
print(delta.days)
