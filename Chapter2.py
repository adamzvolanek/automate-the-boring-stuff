# This is a support python to accompany the Chapter 2 progress
# Specifically starting at Flow Control Statements

# if statements

# Programming Figure 2-3
name = input('Please enter your name: ')
if name == "Alice":
    print('Hi, ', name)
else:
    print('Hello, stranger.')

# Figure 2-4 & Figure 2-5
print('Figure 2-3')
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
    # The purpose of this is to note how an age of 3000 will still print the line above and break
elif age > 100:
    print('You are not Alice, grannie.')

# Figure 2-8 & Figure 2-9
print('\nIntroduction to the while loop')
spam = 0
if spam < 5:
    print('Hello, world using an if statement')
    spam = spam +1

spam = 0
while spam < 5:
    print('Hello, world')
    spam = spam + 1

# Figure 2-10, Annoying While Loop
print('\nAnnoying While Loop')
name = input('Type your name ')
while name != 'your name':
    name = input('Please type your name ')
print('Thank you!')

# Figure 2-11, Introduction to break statements
print('\nIntroduction to break statements')
while True:
    name = input('Please type your name ')
    if name == 'your name':
        break
print('Thank you')

# Figure 2-12 Introduced Continue Statement. A while loop that will while true until false.
print('\nIntroduction to the Continue Statement')
while True:
    name = input('Who are you, Joe? ')
    if name != 'Joe':
        continue

    password = input('Hello, Joe. What is the password? (Hint: It is a fish.) ')
    if password == 'swordfish':
        break
print('Access granted')


# Truthy and Falsey Values
print('\nTruthy and Falsey Values')
name = ''
while not name:
    name = input('Enter your name ')

# Figure 2-13 For Loop with Range
print('\nFor loop with range')
