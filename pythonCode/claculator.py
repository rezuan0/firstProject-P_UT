def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        print("ZeroDivisionError: 'you cannot divide by 0'")
    else:
        return x // y


print(div(-10, 10))