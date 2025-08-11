#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
#falsy means the output must be false
if len('python') == len('dragon'):
    print('Ex 1: ', True)
else:
    print('Ex 1: ', False)

#correct exercise 1
print('Ex 1 (Revised): ', len('python') != len('dragon'))

###############################################################################
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'dragon':
    print ('Ex 2: ', True)
else: 
    print ('Ex 2: ', False)

###############################################################################

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('Ex 3: ','jargon' in 'I hope this course is not full of jargon.')

###############################################################################

#There is no 'on' in both dragon and python
print('Ex 4: ', 'on' not in 'python' and 'dragon')

###############################################################################

#Find the length of the text python and convert the value to float and convert it to string
length = len('python')
print('Ex 5: Length is', length, 'and type is', type(length))
print('Ex 5: Length is', length, 'and type is', type(float(length)))
print('Ex 5: Length is', length, 'and type is', type(str(length)))

###############################################################################
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
if number % 2 == 0:
    print('Ex 6: Even Number')
else:
    print('Ex 6: Odd Number')

###############################################################################
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print('Ex 7: ', (7 // 3) == int(2.7))

###############################################################################
#Check if type of '10' is equal to type of 10

print('Ex 8: ', type('10') == type(10))

###############################################################################
#Check if int('9.8') is equal to 10

print('Ex 9: ', int(9.8) == 10)

