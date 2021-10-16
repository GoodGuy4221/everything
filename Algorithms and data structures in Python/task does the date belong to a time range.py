first_date = {'year': 1957, 'month': 1}

second_date = {'year': 2049, 'month': 9}

year = int(input('Enter year '))
month = int(input('Enter month '))

user_date = {
    'year': year,
    'month': month,
}

if first_date['year'] < user_date['year'] < second_date['year']:
    print('YES!')
elif first_date['year'] == user_date['year']:
    if first_date['month'] < user_date['month']:
        print('YES!')
    else:
        print('NO!')
elif user_date['year'] == second_date['year']:
    if second_date['month'] > user_date['month']:
        print('YES!')
    else:
        print('NO!')
