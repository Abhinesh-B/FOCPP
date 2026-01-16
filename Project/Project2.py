import random

password = input("Enter your password: ")
print()

if len(password) < 9:
    print("Password too short.")
    exit()

for _ in range(3):
    position = random.randint(1, len(password))
    letter = input(f"Enter letter at position {position}: ")
    print()
    
    if letter == password[position - 1]:
        print("Correct")
        print()
    else:
        print("Security check failed.")
        exit()

print("Security check passed.")