class MyException(Exception):
    pass


class TestIntersection(MyException):
    pass


class BoundaryIntersection(MyException):
    pass


MAX_X = 255
MAX_Y = 255


class Triangle:
    def __init__(self, w, h, center):
        if self._center.x > MAX_X:
            raise TestIntersection(self._center)
        self._w, self._h, self._center = w, h, center

    def draw(self):
        if self._center.x - self._center.y > self._w:
            raise BoundaryIntersection(self._center)
        pass


def main(*args):
    pass


if __name__ == '__main__':
    try:
        main()
    except TestIntersection as e:
        print(f'Oh: {e.args}')
        exit(1)
    except ValueError as e:
        print(f'ValueError: {e.args}')
        exit(2)
    except (AttributeError, ZeroDivisionError) as e:
        print(f'Errors: {e.args}')
        exit(3)
    except Exception as e:
        print(f'Unknown error: {e.args}')
        exit(4)
