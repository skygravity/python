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
# is_hot = True
# is_cold = False

# if is_hot:
#         print("It's a hot day")
#         print("Drink plenty of water")
# elif is_cold:
#         print("Is cold outside")
#         print("It's a cold day\nwear warm clothes")
# else:        
#         print("Enjoy your day")
# print("Lucky")

#excersise 

# Price of a house is  1M$
#If buyes has good credit,
#they need to put down 10%
#otherwise
#they need to put down 20%

# good_credit = False    BAD WAY
# bad_credit = True
# put_1 = 10
# put_2 = 20

# if good_credit:
#         print("Down ", put_1)
# elif bad_credit:
#         print("Down ", put_2)
# print("Thank You")

# price = 78000
# has_good_credit = False

# if has_good_credit:
#         down_payment = 0.1 * price
# else:
#         down_payment = 0.2 * price
# print(f"Down payment: {down_payment}")

# --------------------------------------------------------------------------------------------------- 2019 11 21
# Logical Operators 
# ---------------------------------------------------------------------------------------------------------------

# We use it when we have multiple conditions. logical operators: AND; OR

# If applicant has high income and good credit then 
#         Eligible for loan

# good_credit = True
# hight_income = False

# if good_credit or hight_income:
#         print("aeligible for loan")
# else:
#         print("Not eligible")


# If applicant has high income and doesnt have a criminal record then 
#         Eligible for loan

# good_credit = True
# criminal_record = True

# if good_credit and not criminal_record:
#         print("aeligible for loan")
# else:
#         print("Not eligible")

# --------------------------------------------------------------------------------------------------- 2019 11 21
# Comparison Operators 
# ---------------------------------------------------------------------------------------------------------------

# if temperature is > than 30
#         its a hot day
# otherwise if its less than 10
#         its a cold day
# otherwise
#         its neither hot nor cold

# temperature = int(input())

# if temperature > 30:
#         print("its hot day")
# elif temperature < 10:
#         print("its a cold day")
# elif temperature < 30 and temperature > 10:
#         print("its not cold, not hot")

# weight = input("What is your weight?: ")
# kind = input("What kind?: ")
# kg = str('k')
# lbs = str('l')
# if kind is kg and not lbs:
#         print(f"Your weight is {weight} kg")
# else:
#         print(f"Your weight is {weight} punds")

# weight = int(input("Weight: "))
# unit = input("(L)bs or (k)g: ")
# if unit.upper() == "L":
#         converted = weight * 0.45
#         print(f"Your weight is {converted} kg")
# else:
#         converted = int(weight / 0.45)
#         print(f"You are {converted} pounds")

# --------------------------------------------------------------------------------------------------- 2019 11 21
# While Loops 
# ---------------------------------------------------------------------------------------------------------------

# https://www.youtube.com/watch?v=_uQrJ0TkZlc 1:20:50

# i = 1
# while i <= 5:
#         print('*' * i)
#         i = i + 1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#         guess = int(input("Guess: "))
#         guess_count += 1
#         if guess == secret_number:
#                 print(f"You won, secret number is {secret_number}")
#                 break
# else:
#         print(f"You failed, secret number is {secret_number}")
        
# --------------------------------------------------------------------------------------------------- 2019 11 23
# Car Game 
# ---------------------------------------------------------------------------------------------------------------

# Car game, 
# print help -> we get commands for game explained
#         start - to start the Car
#         stop - to stop the Car
#         quit - to exit

#'''start - to start the car; stop - to stop the car; quit - to exit '''
# command = ""
# while True:
#         command = input("> ").lower()
#         if command == "start":
#                 print("Car started...")
#         elif command == "stop":
#                 print("Car stoped...")        
#         elif command == "help":
#                 print("help menu")
#         elif command == "quit":
#                 break
#         else:
#                 print("No comprendo amigo")
        

# --------------------------------------------------------------------------------------------------- 2019 11 24
# Car Game 2
# ---------------------------------------------------------------------------------------------------------------

# condition if car is already started - change message if str is start - > car is already started
# in this case we need to store boolean - if car is started true or false

# command = ""
# started = False
# while True:
#         command = input("> ").lower()
#         if command == "start":
#                 if started:
#                         print("car already started")
#                 else:
#                         started = True
#                         print("Car started...")
#         elif command == "stop":
#                 if not started: 
#                         print("Car already stoped")
#                 else:
#                         started = False
#                         print("Car stoped...")        
#         elif command == "help":
#                 print("help menu")
#         elif command == "quit":
#                 break
#         else:
#                 print("No comprendo amigo")

# --------------------------------------------------------------------------------------------------- 2019 11 24
# For Loops
# ---------------------------------------------------------------------------------------------------------------

# # Simple loop for every number od string:
# for item in "Python":
#         print(item)

# # Simlpe loop for list of strings:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# # Simple loop[ for range 5 (5 not included):
# for item in range(5):
#         print(item)

# # Simple loop[ for range from 5 to 10 (10 not included):
# for item in range(5, 10):
#         print(item)

# # Simple loop[ for range from 5 to 10 with step 2(10 not included):
# for item in range(5, 10, 2):
#         print(item)

# --------------------------------------------------------------------------------------------------- 2019 11 24
# For Loops excercise
# ---------------------------------------------------------------------------------------------------------------

# calculate basket shop total price

# prices = [10, 20, 30]
# total = 0
# for basket in prices:
#         total += basket # 0+10 then 10+20; then 30+30;  total = total + basket
# print(f"Total: {total}")

# --------------------------------------------------------------------------------------------------- 2019 11 24
# Nested Loops 1:47:54
# ---------------------------------------------------------------------------------------------------------------

# for x in range(4):
#         print(x)

# result

# 0
# 1
# 2
# 3

# for x in range(4):
#         for y in range(3):
#                 print(f'({x}, {y})')
# result

# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)
# (3, 0)
# (3, 1)
# (3, 2)

# for x in range(4):
#         for y in range(3):
#                 for z in range(2):
#                         print(f'({x}, {y}, {z})')

# numbers = [5, 2, 5, 2, 2]

# for x in numbers:
#         output = ''
#         for count in range(x):
#                 output += 'x'
#         print(output)

# numbers = [2, 2, 2, 2, 5]

# for x in numbers:
#         output = ''
#         for count in range(x):
#                 output += 'x'
#         print(output)

# --------------------------------------------------------------------------------------------------- 2019 11 25
# Lists 1:56:04
# ---------------------------------------------------------------------------------------------------------------

#  list example -> [1, 2, 3] or [apple, orange, banana]

# names = ['John', 'Bob', 'Sara', 'Vicky']
# print(names)
# # result -> ['John', 'Bob', 'Sara', 'Vicky']

# names = ['John', 'Bob', 'Sara', 'Vicky']
# print(names[0])
# # result -> John

# names = ['John', 'Bob', 'Sara', 'Vicky']
# print(names[-1])
# # result last index in list -> Vicky

# names = ['John', 'Bob', 'Sara', 'Vicky']
# print(names[-2])
# # result second last index in list -> Sara

# names = ['John', 'Bob', 'Sara', 'Vicky']
# print(names[2:])
# # result from two index to the end in list -> ['Sara', 'Vicky']

# names = ['John', 'Bob', 'Sara', 'Vicky']
# for x in names:
#         print(x)
# # result ->
# # John
# # Bob
# # Sara
# # Vicky

# #  we can change values of list
# names[0] = 'Jonas'
# print(names)

# names[4] = 'Nick'
# print(names)
# IndexError: list assignment index out of range

# --------------------------------------------------------------------------------------------------- 2019 11 25
# Lists  excercise 1:59:04
# ---------------------------------------------------------------------------------------------------------------

# write a program to find the largest number in a list [3,6,2,8,4,9,10]

numbers_list = [3, 6, 2, 8, 4, 9, 10]
max_number = numbers_list[0] # we assume that number 0 in list (3) is largest, then if we found bigger one we need to reset it to that number

for number in numbers_list:
        if number > max_number:
                max_number = number
print(max_number)

# --------------------------------------------------------------------------------------------------- 2019 11 25
# 2D list
# ---------------------------------------------------------------------------------------------------------------