def multiply(a, b=None):
    if b is None:   
        return a * a
    return a * b

print(multiply(5))       # 5*5 = 25
print(multiply(5, 3))    # 5*3 = 15
print(multiply(7))       # 49
