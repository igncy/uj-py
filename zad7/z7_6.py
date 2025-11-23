import itertools
import random

class IterA:
    def __init__(self):
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value = 1-self.value
        return self.value


class IterB:
    def __iter__(self):
        return self

    def __next__(self):
        return random.choice('NESW')


class IterC:
    def __init__(self):
        self.value = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.value = 0 if self.value==6 else self.value+1
        return self.value


def iter_test(it, n=20):
    for _ in range(n):
        print(next(it), end=' ')
    print()

iter_test(itertools.cycle([0, 1]))
iter_test(IterA())

iter_test(IterB())

iter_test(itertools.cycle(range(7)))
iter_test(IterC())
