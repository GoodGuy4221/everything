import collections

a = collections.defaultdict(int)

s = 'fdghdhdhfdhgshsh'
for char in s:
    a[char] += 1
print(a)

list_movements_animals = [('cat', 2), ('dog', 5), ('cat', 3), ('dog', 4), ('dog', 3)]
c = collections.defaultdict(list)
for animal, distance in list_movements_animals:
    c[animal].append(distance)
print(c)
