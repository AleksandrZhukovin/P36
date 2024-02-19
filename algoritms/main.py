import timeit
import random


class Algoritms:
    def __init__(self, *args):
        self.array = args
        self.sorted = []

    def buble(self):
        self.sorted = list(self.array)
        n = 0
        while True:
            for i in range(len(self.sorted) - 1):
                if self.sorted[i] > self.sorted[i+1]:
                    n = 1
                    self.sorted[i], self.sorted[i+1] = self.sorted[i+1], self.sorted[i]
            if n == 0:
                break
            n = 0
        return self.sorted

    def selection(self):
        self.sorted = list(self.array)
        min_ = 10000
        n = 0
        while n != len(self.sorted):
            for i in self.sorted[n:]:
                if i < min_:
                    min_ = i
            self.sorted.remove(min_)
            self.sorted.insert(n, min_)
            min_ = 10000
            n += 1
        return self.sorted

    # def insert(self):
    #     self.sorted = list(self.array)
    #     for i in range(1, len(self.sorted)):
    #         while self.sorted[i-1] < self.sorted[i] < self.sorted[i + 1]:
    #             if self.sorted[i-1] > self.sorted[i]:
    #                 self.sorted[i - 1], self.sorted[i] = self.sorted[i], self.sorted[i - 1]
    #             elif self.sorted[i+1] < self.sorted[i]:
    #                 self.sorted[i+1], self.sorted[i] = self.sorted[i], self.sorted[i + 1]
    #     return self.sorted

    def iteration(self):
        self.sorted = list(self.array)
        length = len(self.sorted)
        for i in range(1, length):
            tmp = self.sorted[i]
            j = i
            while (j - 1 >= 0) and (self.sorted[j - 1] > tmp):
                self.sorted[j - 1], self.sorted[j] = self.sorted[j], self.sorted[j - 1]
                j = j - 1
            self.sorted[j] = tmp
        return self.sorted


m = []
for i in range(1000):
    m.append(random.randint(0, 1000))
print(m)
a = Algoritms(*m)
start = timeit.default_timer()
print(a.buble())
print(timeit.default_timer())

start1 = timeit.default_timer()
print(a.selection())
print(timeit.default_timer())

start2 = timeit.default_timer()
print(a.iteration())
print(timeit.default_timer())
