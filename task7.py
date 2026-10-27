password = input("Enter password: ")

upper = False
lower = False
digit = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True

if len(password) >= 8 and upper and lower and digit:
    print("Valid Password")
else:
    print("Invalid Password")
    print("Password must have at least 8 characters,")
    print("an uppercase letter, a lowercase letter,")
    print("and a digit.")