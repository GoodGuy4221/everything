class IterateMe:
    def __init__(self):
        self._items = []
        self._ind = 0

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        self._ind = 0
        return self

    def __next__(self):
        if self._ind < len(self._items):
            self._ind += 1
            return self._items[self._ind - 1]
        raise StopIteration


isinstance = IterateMe()
isinstance.add(52)
isinstance.add(51)
isinstance.add('end')

for e in isinstance:
    print(e)

for e in isinstance:
    print(e)
