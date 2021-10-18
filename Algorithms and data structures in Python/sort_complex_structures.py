test_array = [5, 8, 0, 6, 1, 3, 2, 4, 9, 7]

test_dict = {
    'Varick': ['Varick', 8],
    'Bobole': ['Bobole', 4],
    'Cuckoo': ['Cuckoo', 2],
}

new_list = sorted(test_dict.values(), key=lambda v: v[1])


# print(new_list)


class MyObject:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


obj_1 = MyObject(6)
obj_2 = MyObject(9)

list_obj = [obj_2, obj_1]

next_list = sorted(list_obj, key=lambda o: o.value)
print(next_list)
