start_array = ['this', 'en', 51, True, 0, [], 'range', {}, 'un']
print(start_array)

el_insert = 'el_insert'
insert_index = 2

for i in range(len(start_array)):
    if i >= insert_index:
        start_array[i], el_insert = el_insert, start_array[i]
start_array.append(el_insert)

print(start_array)
