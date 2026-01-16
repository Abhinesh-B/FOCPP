number = input("Enter a number: ")

number = int(number)

print("The numbered entered was", number)

if (number % 2) == 0:
    print("That is an even number")
else:
    print("That is an odd number")

if (number % 10) == 0:
    print("That number is divisible by 10")
else:
    print("That number is not divisible by 10")