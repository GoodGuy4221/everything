from random import randint

matrix = []
len_matrix = 10

for i in range(len_matrix):
    cur_row = []
    for j in range(len_matrix):
        elem = randint(0, 100)
        cur_row.append(elem)
    matrix.append(cur_row)

# print matrix
# for row in matrix:
#     for elem in row:
#         print(f'{elem:02}', end='  ')
#     print()

for row in matrix:
    sum_row = 0
    for elem in row:
        sum_row += elem
        print(f'{elem:03}', end='  ')
    print(f' = {sum_row}')

for i in range(len_matrix):
    sum_col = 0
    for j in range(len_matrix):
        sum_col += matrix[j][i]
    print(sum_col, end='  ')
