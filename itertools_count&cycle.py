from itertools import count, cycle

iter_1 = count(1)
iter_2 = cycle(['r', 'g', 'b'])

# while True:
#     i = next(iter_1)
#     print(i)
#     if i > 9:
#         print('infinity')
#         break
#
# k = 0
# while True:
#     i = next(iter_2)
#     print(i)
#     k += 1
#     if k > 8:
#         print('infinity')
#         break

for i in iter_1:
    print(i)
    if i > 9:
        break
print(f'next - {next(iter_1)}')
print(f'next - {next(iter_1)}...')

for i, e in enumerate(iter_2, 1):
    print(e)
    if i > 8:
        break
print(f'next - {next(iter_2)}')
print(f'next - {next(iter_2)}')
print(f'next - {next(iter_2)}...')
