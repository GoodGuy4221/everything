number_students = int(input('Number of students: '))
students = {}
sum_value = 0

for i in range(number_students):
    full_name = input(f'Name and surname of student #{i + 1} ')
    assessment = float(input(f'Assessment of student #{i + 1} '))
    students.update({full_name: assessment})
    sum_value += assessment

average_assessment = sum_value / number_students

print(f'{average_assessment =}')

for key, value in students.items():
    if value > average_assessment:
        print(f'{key} - {value}')
