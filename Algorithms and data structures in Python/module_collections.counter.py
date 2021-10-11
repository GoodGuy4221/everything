from collections import Counter

a = Counter()
print(a)
b = Counter('ffsdfgdsggsdfgddsdhdfdfhgsdh')
print(b)
print(b.most_common(2))

c = Counter(a=5, b=-9, c=-2)
d = Counter(a=4, b=-2, c=3)
print(c, d, sep='\n')

print('c+d', c + d)
print('c-d', c - d)
print('c&d', c & d)
print('c|d', c | d)
