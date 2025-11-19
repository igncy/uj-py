import itertools

'''
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia]. 
'''

def iter_test(it, n=20):
    i=0
    while i<n:
        print(next(it), end=' ')
        i+=1
    print()


class IterA:
    def __init__(self):
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value = 1-self.value
        return self.value


class IterB:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

class IterC:
    def __init__(self):
        self.value = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.value = 0 if self.value==6 else self.value+1
        return self.value


iter_test(itertools.cycle([0, 1]))
iter_test(IterA())

iter_test(IterB())

iter_test(itertools.cycle(range(7)))
iter_test(IterC())
