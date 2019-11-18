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


#-------------------------------------------------------------------------------------------------------------------------------

course = 'python for beginners'
# Calculates number of characters in the string
# len() is general purpose function
# course. -> is function, but we reffer it as methods

# if function  reffers to something we say it's method. For example course.upper() -> function upper() reffers to string course so its a method
# so print(len()) is general purpose functions, they don't bellong to string

# print(len(course))
# print(course.upper()) # Makes all letters capital -> PYTHON FOR BEGINNERS
# print(course.capitalize()) # Starts from Capital letter -> Python for beginners
# print(course.find('h')) # finds string symbol and shows like index -> 3
print(course.replace('beginners', 'Absolute Beginners'))

# https://www.youtube.com/watch?v=_uQrJ0TkZlc 45:48




