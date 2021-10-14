a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

search_num = 22
left_pos = 0
right_pos = len(a) - 1
middle_pos = len(a) // 2
founded = False

while left_pos <= right_pos:
    if search_num > a[middle_pos]:
        left_pos = middle_pos + 1
    elif search_num < a[middle_pos]:
        right_pos = middle_pos - 1
    else:
        print('Number is here!')
        founded = True
        break
    middle_pos = (left_pos + right_pos) // 2

if not founded:
    print('Number is not here!')
