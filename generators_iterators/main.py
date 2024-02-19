# a = [1, 2, 3, 4]
#
# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
#
# for b in i:
#     print(b)
# for b in i:
#     print(b)
# print(next(i))


# class Iter:
#     def __init__(self, start, finish, step):
#         self.start = start
#         self.finish = finish
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start >= self.finish:
#             raise StopIteration
#         self.start += self.step
#         return self.start
#
#
# i = Iter(0, 10, 2)
# print(next(i))
# for v in i:
#     print(v)
# # написати ітератор чисел від 0 до 1000 з кроком 50
# # створити ітератор аналог range але який повертає значення в зворотньому порядку
#
#
# def gen(a, c, b=10):
#     n = 0
#     while n != a:
#         n += 1
#         yield n
#
#
# g = gen(10, 2)
#
# print(next(g))
# print(next(g))
#
# for i in g:
#     print(i)
#
# for a in gen(10):
#     print(a)
# написати копію рендж
# написати генератор масивів (повертати на кожну ітерацію масив з +1 елементом)
# модифікувати вказати крок із яким будуть записані числа в масиві
# написати генератор чисел фібоначі   1 1 2 3 5 8 13 21

# def rg(finish, start=None, step=1):
#     if start: finish, start = start, finish
#     while start < finish:
#         yield start
#         start += step
#
#
# for i in rg(5, 15, 3):
#     print(i)
#
#
def mg(l, step=1):
    m = []
    i = 0
    while len(m) != l:
        m.append(i)
        yield m
        i += step


for a in mg(5):
    print(a)
#
#
# def fg(l):
#     n = 3
#     fibonachi = [1, 1]
#     while n != l:
#         fibonachi.append(fibonachi[n-1] + fibonachi[n-2])
#         yield fibonachi[n-1] + fibonachi[n-2]
#         n += 1
