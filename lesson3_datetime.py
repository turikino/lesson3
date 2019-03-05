from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU')



date_now = datetime.now()
print("Сейчас: {}.".format(date_now.strftime('%A %d.%m.%Y %X')))
today = datetime.today()
print("Сегодня: {}.".format(today.strftime('%A %d.%m.%Y %X')))
yesterday = today - timedelta(days = 1)
print("Вчера: {}.".format(yesterday.strftime('%A %d.%m.%Y %X')))
month_ago = today - timedelta(days = 30)
print("Месяц назад: {}.".format(month_ago.strftime('%A %d.%m.%Y %X')))