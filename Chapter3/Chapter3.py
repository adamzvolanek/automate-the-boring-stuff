def hello():
    print("Howdy")
    print("Howdy!!!!")
    print("Hello there.")


hello()


def hello(name):
    print("Hello, " + name)


hello("Alice")
hello("Bob")

# print("Hello", end=" ")
# print("World")

print("cats", "dogs", "mice", sep=".")


# def spam():
    # bacon()
    # print(eggs)


def bacon():
    # ham = 101
    # eggs = 0


eggs = 42
spam()
print(eggs)


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Divide by zero error, invalid argument")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
