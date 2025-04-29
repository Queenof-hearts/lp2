# This Python code simulates a simple interactive chatbot that engages the user in conversation and asks basic questions.

# 🔸 Function-wise Explanation
# greet(bot_name, birth_year)

# Introduces the chatbot using its name and creation year.

# remind_name()

# Asks the user for their name and compliments it.

# guess_age()

# Uses the Chinese Remainder Theorem to guess the user's age.

# Asks for the remainders when dividing the age by 3, 5, and 7.

# Formula:

# python
# Copy
# Edit
# age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
# count()

# Demonstrates counting ability by printing numbers from 0 to a user-specified value.

# test()

# A multiple-choice quiz asking: "Why do we use methods?"

# Loops until the correct answer (2) is entered.

# end()

# Displays a congratulatory message and ends the conversation.

# 🔸 Sample Output
# vbnet
# Copy
# Edit
# Hello! My name is TE-Chatbot.
# I was created in 2022.
# Please, remind me your name.
# > Yash
# What a great name you have, Yash!
# Let me guess your age...
# ...
# Your age is 21; that's a good time to start programming!
# ...
# Let's test your programming knowledge.
# Why do we use methods?
# ...
# 2
# Completed, have a nice day!
# 🔸 Features
# Covers input/output, loops, functions, conditionals, and basic logic.

# Great beginner-level Python project.

def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0}; that's a good time to start programming!".format(age))

def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    print('Completed, have a nice day!')
    print('.')
    print('.')
    print('.')

def end():
    print('Congratulations, have a nice day!')
    print('.')
    print('.')
    print('.')
    input()

# Running the chatbot
greet('TE-Chatbot', '2022')  # You can change the name or year if needed
remind_name()
guess_age()
count()
test()
end()
