import calendar_creator

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4,
          'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10, 'November': 11, 'December': 12}

year = 2023
my_month = 'February'

base_salary = 29529
current_month_hours = 176
worth_per_hour = base_salary / current_month_hours
worth_for_night = worth_per_hour * 1.4
extra_holidays_factor = 1

print('Базовая оплата в час = ', round(worth_per_hour, 2))


current_month = calendar_creator.month_creator(months[my_month], year)
print(current_month)