# def counter_generator(count):
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# counter1 = counter_generator(0)
# print(counter1())
# print(counter1())
# print(counter1())
#

def counter_generator(a,b=1):
    count = a
    def increment():
        nonlocal count
        count += b
        return count
    return increment
counter2 = counter_generator(10,2)
print(counter2())
print(counter2())
print(counter2())

counter1 = counter_generator(0)
print(counter1())
print(counter1())
print(counter1())

