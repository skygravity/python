# course = 'Python for beginners'
# print(course)
# # Use double quotes to have single quote in the middle
# course_str = "Python's for beginners"
# print(course_str)
# #  Vice versa
# course_str_kinda = 'Python for "beginners"'
# print(course_str_kinda)
# # Multiline string using three quotes ''' or """
# course_str_email = '''
# Dear User
# Python's for beginners is awesome

# Thank You
# '''
# print(course_str_email)
# # Sting indexes as follows
# # Python
# # 012345
# python = 'Python'
# print(python[1]) #we should get y
# print(python[-1]) #we should get first symbol from back (unique for Python)
# print(python[0:3]) #we should get first three symbols

# name = 'Vytautas'
# print(name[1:-1])
# # result - ytauta
# print(name[:-1])
# print(name[1:])
# print(name[:])

# Formated Strings

# https://www.youtube.com/watch?v=_uQrJ0TkZlc 39:10

        # first = 'John'
        # last = 'Doe'
        # message = first + ' [' + last + '] is a coder'
        # msg = f'{first} [{last}] is a coder' #this is formated string
        # print(msg)


# --------------------------------------------------------------------------------------------------- 2019 11 17
# String Functions and Methods
# ---------------------------------------------------------------------------------------------------------------

# course = 'python for beginners'
# Calculates number of characters in the string
# len() is general purpose function
# course. -> is function, but we reffer it as methods

# if function  reffers to something we say it's method. For example course.upper() -> function upper() reffers to string course so its a method
# so print(len()) is general purpose functions, they don't bellong to string

# print(len(course))
# print(course.upper()) # Makes all letters capital -> PYTHON FOR BEGINNERS
# print(course.capitalize()) # Starts from Capital letter -> Python for beginners
# print(course.find('h')) # finds string symbol and shows like index -> 3
# print(course.replace('beginners', 'Absolute Beginners'))

# https://www.youtube.com/watch?v=_uQrJ0TkZlc 45:48

# This will return boolean true of false. there is 'python' in course string. Define and 'in' methods is different, define searches index of haracter; 'in' is boolean.

# course = 'python for beginners'
# print('@' in course)


# --------------------------------------------------------------------------------------------------- 2019 11 18
# Integers and Floats 48:54
# ---------------------------------------------------------------------------------------------------------------

# Integer 10
# Float 10.123

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 | 3)
# print(10 ** 3)
# print(10 % 3)
# print(10 ^ 3)

# We can increment integers
# x = 10
# x = 10 + 3
# print(x)
# result x = 13

# Same - augmented asigment operator
# x = 10
# x += 3
# print(x)
# same result x = 13

# x = 10 + 3 * 2
# print(x)
# result is 16

# x = 10 + 3 * 2 ** 2
# print(x)
# result is 22

# x = 2.9
# print(round(x))
# result 3

# print(abs(-2.8))      Absolute function - will return positive number
# result 2.8

# import math
# print(math.ceil(2.9))
# 3

# --------------------------------------------------------------------------------------------------- 2019 11 18
# If statements
# ---------------------------------------------------------------------------------------------------------------

# if it's hot day
#       It's a Hot day
#       Drink plenty of water
# otherwise if it's cold
#       its'a cold day
#       wear warm clothes
# otherwise
#       it's a lovely day

#  We need to define boolean
is_hot = False

if is_hot:
        print("It's a hot day")
        print("Drink plenty of water")
else:
        print("It's a cold day\nwear warm clothes")
print("Enjoy your day")

# --------------------------------------------------------------------------------------------------- 2019 11 19
# If statements
# ---------------------------------------------------------------------------------------------------------------