from countries import countries
from countries_data import countries_data

#Iterate 0 to 10 using for loop, do the same using while loop.

for i in range(0,11):
    print(i)

print()

i = 0

while i < 11:
    print(i)
    i += 1

print()

#Iterate 10 to 0 using for loop, do the same using while loop.

for i in range(10, -1, -1):
    print(i)

print()

i = 10

while i > -1:
    print(i)
    i -= 1

print()

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
i = 1
while i < 8:
    print('#' * i)
    i+=1

print()

for row in range(8):
    for column in range(8):
        print('# ', end='')
    print()  # New line after each row

print()

#create the following multiplication pattern

for digit in range (0, 11):
    print(f'{digit} x {digit} = {digit * digit}')

print()
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

item_list =  ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in item_list:
    print(item)

print()

#Use for loop to iterate from 0 to 100 and print only even numbers
#if want odd, change step the starting and ending numbers in range

for i in range (0, 101, 2):
    print(i)

print()

list_numbers = []
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
for i in range (0, 101):
    list_numbers.append(i)

print(sum(list_numbers))

print()

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_list = []
odd_list = []

for i in range(0, 101):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f'The sum of all evens is {sum(even_list)}. And the sum of all odds is {sum(odd_list)}.')
print()

for country in countries:
    if 'land' in country:
        print(country)

print()

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fruits = ['banana', 'orange', 'mango', 'lemon']
new_list = []

for i in range(len(fruits) - 1, -1, -1):
    print(fruits[i])
    new_list.append(fruits[i])
print(new_list)

print()

'''Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world'''


language_list = []
for entry in countries_data:
    for language in entry['languages']:
        language_list.append(language)
print(len(set(language_list)))

count_dict = dict.fromkeys(sorted(set(language_list)), 0)

for language in language_list:
    count = language_list.count(language)
    count_dict[language] = count
print(count_dict)
print()
sorted_count_dict = sorted(count_dict.items(), key = lambda x: x[1], reverse=True)
print(sorted_count_dict[:10])


