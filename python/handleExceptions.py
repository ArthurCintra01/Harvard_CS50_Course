import sys

#handling exception invalid input (caso o usuario passe um valor que nao seja int)
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input.")
    sys.exit(1) #exit status 1 (error)

#handling exception division by 0
try:
    result = x/y
except ZeroDivisionError:
    print("Error: cannot divide by 0.")
    sys.exit(1) #exit status 1 (error)

print(f"{x} / {y} = {result}")