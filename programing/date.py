from __future__ import division
mouths = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

ending = ['st', 'nd', 'rd'] + 17 * ['th'] \
       + ['st', 'nd', 'rd'] + 7 *['th'] \
       + ['st']

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

mouth_number = int(month)
day_number = int(day)

mouth_name = mouths[mouth_number-1]
day_name = day + ending[day_number-1]

print mouth_name + ' ' + day_name + '. ' + year

