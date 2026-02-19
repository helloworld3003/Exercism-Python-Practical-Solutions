def square(number):
    if number in range(1,65):
        return 2**(number-1) if number>1 else 1
    raise ValueError("square must be between 1 and 64")


def total():
    t=0
    for i in range(1,65):
        t+=square(i)
    return t