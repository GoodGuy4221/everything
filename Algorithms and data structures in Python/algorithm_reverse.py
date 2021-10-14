start_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(start_array)

for i in range(len(start_array) // 2):
    start_array[i], start_array[len(start_array) - i - 1] = start_array[len(start_array) - i - 1], start_array[i]

print(start_array)
