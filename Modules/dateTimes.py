from datetime import datetime

birthday = datetime(1992, 12, 14)
print(birthday.day)
print(birthday.weekday())
print(birthday.month)
print(datetime.now() - datetime(2020, 10, 16))

# --------------------------------------------------------------------------------

parsed_date = datetime.strptime('Jun 3, 2020', '%b %d, %Y')
print(parsed_date.month)


# --------------------------------------------------------------------------------

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
