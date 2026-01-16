import sys

count = len(sys.argv)
total = 0

while count > 1:
    count -= 1
    total += float(sys.argv[count])

print("Total is", total)

# Calculate and print the average

if len(sys.argv) > 1:
    average = total / (len(sys.argv) - 1)
    print("Average is", average)