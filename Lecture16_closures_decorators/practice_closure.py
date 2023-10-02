#
# def counter():
#     count = 0
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#     return inc
# f1 = counter()
# f2 = counter()
# print(f1())
# print(f1())
# print(f1())
# print(f2())
#

#
# def outer(n):
#     def inner(x):
#         return x + n
#     return inner
# add_1 = outer(1)
#
# print(add_1(10))
# print(add_1(30))

# Nested Closure

def increment(n):
    def inner(start):
        current = start
        def inc():
            nonlocal current
            current += n
            return current
        return inc
    return inner
# (inner)
fn = increment(2)
print(fn.__code__.co_freevars)
print(fn.__closure__)


# (inc)
inc = fn(100)
print(inc())
print(inc())
print(inc.__code__.co_freevars)
print(inc.__closure__)
