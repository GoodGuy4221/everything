def generator_range(start, stop, step=1):
    next_el = start
    while next_el < stop:
        yield next_el
        next_el += step


g = generator_range(0, 10)
print(type(g))

for i in g:
    print(i)
