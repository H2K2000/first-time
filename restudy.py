# x = 10
# y = 0
# L = [1, 2, 3]
#
# try:
#     # a[0]
#     a = x / 2
#     l[10]
# except ZeroDivisionError as t:
#     print(t,1)
# except NameError as t1:
#     print(t, 2)
# except Exception as t2:
#     print(t, 3)
# else:
#     print(a)
# finally:
#     print('finsh')

# class AgeError(Exception):
#     ...
#
#
# age = 17
# if age >= 18:
#     print('ok')
# else:
#     raise AgeError('age must be over 18')

# write a Python program that implement a decorator to provide caching with expiration time for a function

# import time
#
#
# def timer(func):
#     def inner(*args, **kwargs):
#         t = time.time()
#         res = func(*args, **kwargs)
#         print(round(time.time() - t, 2), 'seconds')
#         return res
#     return inner
#
# @timer
# def summa(n):
#     k = 0
#     for i in range(n + 1):
#         k += 1
#     return k
#
#
# print(summa(100_000_000))
# class Animal:
#     breath = True
#     eys = True
#
#     def __init__(self, names, legs, color):
#         self.names = names
#         self.legs = legs
#         self.color = color
#
#     def sleep(self):
#         print(print(f"{self.names} sleeps."))
#
#
# class Cats(Animal):
#     tail = True
#
#     def __init__(self, name, color, color_nums):
#         super().__init__(name, 4, color)
#         self.color_nums = color_nums
#
#     def eat(self):
#         print(f"{self.names} eats.")
#
#     def scratch(self):
#         print(f"{self.names} scratches.")
#
#
# class Lion(Cats):
#     def __init__(self, names, color):
#         super().__init__(names, color, 1)
#
#     def swim(self):
#         print(f"{self.names} swims.")
#
#
# l1 = Lion("simba", "yellow")
# l1.sleep()
# l1.eat()
# l1.scratch()
# l1.swim()

# class


print('hello', 10, 'somthing')
print([10, 29, 14,36])
