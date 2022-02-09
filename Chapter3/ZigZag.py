# Small animation program to create a back-and-forth zigzag pattern
# Will operate until stop is requested or Ctrl+C

import sys


# String to print
def zigzag():
    print("********")
    return None


indent = 0
indentIncreasing = True

try:
    while True:
        print(" " * indent, end="")
        print("********")

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False

        else:
            indent = indent - 1

            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    pass

try:
    while True:
        for i in range(19):
            print(" " * indent, end="")
            print("xxxxxxxxx")
            indent = i + 1
        for i in range(19, 0, -1):
            print(" " * indent, end="")
            print("xxxxxxxxx")
            indent = i - 1

except KeyboardInterrupt:
    sys.exit()
