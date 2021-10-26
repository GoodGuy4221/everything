class IterateMeIterator:
    def __init__(self, items):
        self._items = items
        self._ind = 0

    def __next__(self):
        if self._ind < len(self._items):
            self._ind += 1
            return self._items[self._ind - 1]
        raise StopIteration


class IterateMe:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        return IterateMeIterator(self._items)


isinstance = IterateMe()
isinstance.add(52)
isinstance.add(51)
isinstance.add(50)

for e in isinstance:
    print(e)
