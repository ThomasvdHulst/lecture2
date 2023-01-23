import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("please enter a number")
    sys.exit(1)

try:
    result = x/y
except:
    print("Error cannot divide by zero")
    sys.exit(1)

print(result)