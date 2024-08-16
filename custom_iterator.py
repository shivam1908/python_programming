class Counter2:
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self._current = start
    
    def __iter__(self):
        return self
    def __next__(self):
        if self._current < self._end:
            current = self._current
            self._current += 2
            return current
        else:
            raise StopIteration
    def __repr__(self):
        return "Counter from start to end inclusive with step of 2"

steps = Counter2(1,10)
for num in Counter2(1,10):
    print(num)

