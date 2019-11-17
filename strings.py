course = 'Python for beginners'
print(course)
# Use double quotes to have single quote in the middle
course_str = "Python's for beginners"
print(course_str)
#  Vice versa
course_str_kinda = 'Python for "beginners"'
print(course_str_kinda)
# Multiline string using three quotes ''' or """
course_str_email = '''
Dear User
Python's for beginners is awesome

Thank You
'''
print(course_str_email)
# Sting indexes as follows
# Python
# 012345
python = 'Python'
print(python[1]) #we should get y
print(python[-1]) #we should get first symbol from back (unique for Python)
print(python[0:3]) #we should get first three symbols

name = 'Vytautas'
print(name[1:-1])
# result - ytauta
print(name[:-1])
print(name[1:])
print(name[:])

# Formated Strings

# https://www.youtube.com/watch?v=_uQrJ0TkZlc 39:10

first = 'John'
last = 'Doe'
message = first + ' [' + last + '] is a coder'
print(message)

