list_a = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 9, 0, 0]

for i in range(len(list_a)):
    duplicated_founded = False
    for j in range(len(list_a)):
        if list_a[i] == list_a[j] and not i == j:
            duplicated_founded = True
            break
    if duplicated_founded:
        print(list_a[i])
    # if not duplicated_founded:
    #     print(list_a[i])
