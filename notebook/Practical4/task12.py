to_seconds = lambda hours, minutes=0: hours*3600 + minutes*60

print(to_seconds(1))  # 3600

print(to_seconds(2))  # 7200

print(to_seconds(1, 30)) # 5400
