from datetime import datetime, timedelta

# 1. Вычесть пять дней из текущей даты
def subtract_five_days():
    return datetime.today() - timedelta(days=5)

print("Five days ago:", subtract_five_days().date())

# 2. Вчера, сегодня, завтра
def yesterday_today_tomorrow():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return yesterday.date(), today.date(), tomorrow.date()

y, t, tm = yesterday_today_tomorrow()
print("Yesterday:", y)
print("Today:", t)
print("Tomorrow:", tm)

# 3. Удаление микросекунд
def drop_microseconds(dt):
    return dt.replace(microsecond=0)

current_dt = datetime.now()
print("Datetime without microseconds:", drop_microseconds(current_dt))

# 4. Разница между двумя датами в секундах
def date_difference_in_seconds(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 12, 0, 0)
print("Difference in seconds:", date_difference_in_seconds(date1, date2))
