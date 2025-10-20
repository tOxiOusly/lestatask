
"""------------------------Первое задание------------------------"""

def isEven(value):
    return (value & 1) == 0

"""--------------------------------------------------------------"""


"""------------------------Второе задание------------------------"""

"""Реализация 1"""

class CircularBufferList:
    def __init__(self, capacity: int):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    def push(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity
    def front(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        return item
    def pop(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
    def __repr__(self):
        return (f"CircularBufferList(buffer={self.buffer}, "
                f"head={self.head}, tail={self.tail}, size={self.size})")

"""Реализация 2"""

from collections import deque

class CircularBufferDeque:
    def __init__(self, capacity: int):
        self.buffer = deque(maxlen=capacity)
    def push(self, item):
        self.buffer.append(item)
    def pop(self):
        if not self.buffer:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()
    def __repr__(self):
        return f"CircularBufferDeque({list(self.buffer)})"

"""--------------------------------------------------------------"""


"""------------------------Третье задание------------------------"""

import random
import timeit
import numpy as np

data_random = random.sample(range(10_000), 10_000)
data_sorted = list(range(10_000))

def timsort(arr):
    return sorted(arr)

def quicksort(arr):
    return np.sort(arr, kind='quicksort')

def mergesort(arr):
    return np.sort(arr, kind='mergesort')

def heapsort(arr):
    return np.sort(arr, kind='heapsort')

def measure(func, data):
    return timeit.timeit(lambda: func(data[:]), number=3)


print (f"  TimSort (rand)  : {measure(timsort, data_random):.4f} сек")
print (f"  TimSort (sorted)  : {measure(timsort, data_sorted):.4f} сек")

print (f"  Quicksort (rand)  : {measure(quicksort, data_random):.4f} сек")
print (f"  Quicksort (sorted)  : {measure(quicksort, data_sorted):.4f} сек")

print (f"  Mergesort (rand)  : {measure(mergesort, data_random):.4f} сек")
print (f"  Mergesort (sorted)  : {measure(mergesort, data_sorted):.4f} сек")

print (f"  Heapsort (rand)  : {measure(heapsort, data_random):.4f} сек")
print (f"  Heapsort (sorted)  : {measure(heapsort, data_sorted):.4f} сек")

"""--------------------------------------------------------------"""