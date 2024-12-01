
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print("Can not divide on zero")
