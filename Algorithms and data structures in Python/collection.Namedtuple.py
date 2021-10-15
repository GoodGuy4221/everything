from collections import namedtuple

my_namedtuple = namedtuple('my_namedtuple', ['a', 'b', 'c'])

my_instance = my_namedtuple(a=2, b=4, c=8)
print(my_instance)
my_instance_1 = my_instance._replace(a=16)
print(f'{my_instance.b=}\n{my_instance_1.a=}')
print(f'{my_instance[1]=}\n{my_instance_1[0]=}')
