from collections import Counter

my_counter = Counter(a=9, b=2, c=12, d=-2)
my_counterR = Counter(a=4, b=1, c=9)
print(my_counter)
print(*my_counter.elements())
print(my_counter.most_common())
print(my_counter.most_common(2))
my_counter.subtract(my_counterR)
print(my_counter)

print(f'В порядке наименее встречающихся элементов {my_counter.most_common()[::-1]=}')
print(f'{my_counter.most_common()[:-2:-1]=}')

# удалить элементы которые встречаются менее одного раза
my_counter += Counter()
print(f'удалить элементы которые встречаются менее одного раза {my_counter}')

print(sum(my_counter.values()))
print(list(my_counter))
my_counter.clear()
print(my_counter)
