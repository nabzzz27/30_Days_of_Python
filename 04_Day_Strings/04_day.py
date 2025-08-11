#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
print(a + ' ' + b + ' ' + c + ' ' + d)
print()

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a, b, c = 'Coding', 'For', 'All'
print(f'{a} {b} {c}')
print()

#Declare a variable named company and assign it to an initial value "Coding For All" and print it
# Print the length of the company string using len() method and print().
# Change all the characters to uppercase letters using upper() method.
# Change all the characters to lowercase letters using lower() method.
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize()) #capitalize first letter of whole string
print(company.title()) #capitalize first letter of every word of whole string
print(company.swapcase()) #swaps casing of original string to opposite
print()

#Cut(slice) out the first word of Coding For All string.
print(company[:7])
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
coding = 'Coding'
print(coding in company)
print(company.find('Coding'))
print(company.index('Coding'))
#print(company.index('coding')) will raise value error
print()

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
#Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace('Coding', 'Python').replace('All', 'Everyone'))
print()

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string.split(', '))
print()

#What is the character at index 0 in the string Coding For All.
print(company[0])
#What is the last index of the string Coding For All.
print(company[-1])
#What character is at index 10 in "Coding For All" string.
print(company[10]) #at index 0, it is a whitespace
print()

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
python = 'Python For Everyone'
python_split = python.split(' ')
print(f'{python_split[0][0]}.{python_split[1][0]}.{python_split[2][0]}')

#Create an acronym or an abbreviation for the name 'Coding For All'.
company_split = company.split(' ')

for word in company_split:
    print(word[0], end='')

print()
print('.'.join(word[0] for word in company_split))
print()

#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding For All People'
print(string.rfind('l'))
print()

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because because because'))
print(string[31:31 + 1 + len('because because because')])
print()

#Does ''Coding For All' start with a substring Coding?
string = 'Coding For All'
print(string.startswith('Coding'))
#Does 'Coding For All' end with a substring coding?
print(string.endswith('coding'))
print()

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip(' '))
print()

string_1 = '30DaysOfPython'
string_2 = 'thirty_days_of_python'
print(string_1.isidentifier())
print(string_2.isidentifier())
print()

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(list))
print()

#Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\n' \
'I just wonder what is next.')
print()

#Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity\n' \
'Nabil\t250\tFinland\tHelsinki')
print()

#Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {int(area)} meters square.')
print()

#Make the following using string formatting methods:
a = 8
b = 6

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {round(a / b, 2)}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')


