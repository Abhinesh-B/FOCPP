to_seconds = lambda hours, minutes: hours*3600 + minutes*60

print(to_seconds(0, 2))    # 120 

print(to_seconds(2, 0))    # 7200

print(to_seconds(1, 30))   # 5400

