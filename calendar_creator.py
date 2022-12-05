

# Returns a dictionary with days of current month of year
def month_creator(month, year):
    month_table_365 = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    month_table_366 = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    month_table = month_table_365.copy()
    all_days = 0

    for current_year in range(2022, year):
        if current_year % 4 == 0:
            month_table = month_table_366.copy()
        else:
            month_table = month_table_365.copy()
        if current_year < year:
            all_days += month_table[11]

    if year % 4 == 0:
        month_table = month_table_366.copy()
    else:
        month_table = month_table_365.copy()

    all_days += 1  # First day of January of this year.
    if month - 1 > 0:
        # First day of current month of this year.
        all_days += month_table[month - 2]
    day_differnece = {1: 'Saturday', 2: 'Sunday', 3: 'Monday', 4: 'Tuesday',
                      5: 'Wednesday', 6: 'Thursday', 7: 'Friday'}
    day_of_begin_month = all_days - ((all_days - 1) // 7) * 7
    days_in_month = 31
    if month - 1 > 0:
        days_in_month = month_table[month - 1] - month_table[month - 2]

    days = {}
    day_of_week = day_of_begin_month
    for i in range(0, days_in_month):
        days[i + 1] = day_differnece[day_of_week]
        day_of_week += 1
        if day_of_week > 7:
            day_of_week = 1

    for key in list(days.keys()):
        if days[key] in ('Saturday', 'Sunday'):
            days[key] = days[key] + '_extra'
        else:
            days[key] = days[key] + '_common'

    return days





