import datetime

date_one = 'Jan 15, 2023 - 12:05:33'

date_for_pyhon = datetime.datetime.strptime(date_one, '%b %d, %Y - %H:%M:%S')
print(date_for_pyhon)
print(date_for_pyhon.strftime('%B'))
print(date_for_pyhon.strftime('%d.%m.%Y, %H:%M'))
