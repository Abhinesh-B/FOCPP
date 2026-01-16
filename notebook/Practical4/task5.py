def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        max_val = a
    else:
        max_val = b
    return max_val

print(findMax(3, 9))
print(findMax(20, 15))
print(findMax(-5, -1))
