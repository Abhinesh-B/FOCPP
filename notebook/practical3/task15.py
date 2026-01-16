numbers = [10, 20, 30, 90, 200, 30, 22, 11]
total = 0
for n in numbers:
    if n > 100:
        break
    total += n
    print(total)
