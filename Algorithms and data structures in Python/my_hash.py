h_list = [None] * 26


def my_hash(value):
    hash_ = ord(value[0]) - ord('a')
    h_list[hash_] = value
    print(h_list)


a = 'apple'
my_hash(a)
b = 'banana'
my_hash(b)
c = 'ananas'
my_hash(c)

print(4567 == 4 * 10 ** 3 + 5 * 10 ** 2 + 6 * 10 ** 1 + 7 * 10 ** 0)


def my_hash_2(value):
    letter = 26
    hash_ = 0
    size = 10_000
    for index, char in enumerate(value):
        hash_ += (ord(char) - ord('a') + 1) * letter ** index
    return hash_ % size


print(my_hash_2(a))
print(my_hash_2(b))
print(my_hash_2(c))
