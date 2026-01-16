# import random

# def main() -> None:
#     password = input("Enter your password: ")

#     if len(password) < 9:
#         print("\nPassword too short.")
#         return

#     for _ in range(3):
#         # Positions shown to the user are 1-based (first character is position 1)
#         pos = random.randint(1, len(password))
#         answer = input(f"\nEnter letter at position {pos}: ")

#         # Treat anything other than exactly one matching character as incorrect
#         if len(answer) != 1 or answer != password[pos - 1]:
#             print("\nSecurity check failed.")
#             return

#         print("\nCorrect")

#     print("\nSecurity check passed.")

# if __name__ == "__main__":
#     main()


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