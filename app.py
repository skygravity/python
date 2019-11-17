print('Vytautas')
print('o----')
print(' ||||')
print('*' * 10)

# variables - used to store data into computers memory; variable is a label for a location in memory.
# example;
price = 10
# price - name of our variable (identifier)
# 10 - value. before it stores to memory it goes through, before storing its converted to binary representation.
# we can update our variable (Number 20 is integer)
price = 20
# define another variable (4.9 is floating point number)
rating = 4.9
# string
name = 'Vytautas'
#boolean (true, false)
smart = True
# separate variables name if more than two words
is_published = True

# python will alocate some memory and store data - "price";
print(price) #use without quatation " ; output should be 20; 14:15 https://www.youtube.com/watch?v=_uQrJ0TkZlc

# Excercise
# "We check in a patient named John Doe. He's 20 years old and is a new patient"
        # name = "John Doe"
        # age = 20
        # is_new = True

        # name = input('What is your name? ')
        # print('Hi ' + name) # + sign means we concatenating this string with input. In another words - this means expression with value

# Excercise 2
# Ask two questions:person's name and favorite color. Then, print a message like "Mosh likes blue"
        # name = input('What is your name? ')
        # fav_color = input('What is your favorite color? ')
        # print(name + ' likes ' + fav_color)

# Excercise 3
        # birth_year = input('Birth year: ')
        # print(type(birth_year))
        # age = 2019 - int(birth_year)
        # print(type(age))
        # # birth_year = 2019 - '1980' integer minus string, py don't know what to do
        # #  we neet to convert string '1980' into integer with int('This converts strings into integers') 
        # print(age)

# Excercise 4
# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal
weight_kg = input('Weight (kg)? ')
weight_lbs = int(weight_kg) * 2.2
print(weight_lbs)

