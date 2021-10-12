import sys


def show_this(object_):
    print(f'{type(object_)=}, {sys.getsizeof(object_)=}, {sys.getrefcount(object_)=}, {object_=}')


def walk_object(object_):
    if hasattr(object_, '__iter__'):
        if hasattr(object_, 'items'):
            for key, value in object_.items():
                show_this(key)
                show_this(value)
        else:
            for item in object_:
                show_this(item)
    else:
        show_this(object_)


walk_object('hello')
walk_object(51)
print('*' * 51)
test_list = [i for i in range(1, 10, 2)]
show_this(test_list)
walk_object(test_list)
show_this(tuple(test_list))
print('*' * 51)
test_dict = {i: i for i in range(0, 11, 2)}
show_this(test_dict)
walk_object(test_dict)
