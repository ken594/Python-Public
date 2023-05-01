### Section 26: *args = parameter that will pack all arguments into a tuple
#               useful so that a function can accept a varying amount of arguments


def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))