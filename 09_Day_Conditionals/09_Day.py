#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input('Enter your age: '))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f'You need {18 - age} more year(s) to learn to drive.')

print()

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
age = int(input('Enter your age: '))
other_age = 25

if age == other_age:
    print('We are the same age.')
elif age > other_age:
    if age - other_age == 1:
        print('You are 1 year older than me.')
    else:
        print(f'You are {age - other_age} years older than me.')
else:
    if other_age - age == 1:
        print('You are 1 year younger than me.')
    else:
        print(f'You are {other_age - age} years younger than me.')

print()

#Write a code which gives grade to students according to theirs scores:
score = int(input("Enter you score: "))

if score >= 80:
    print('A')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C')
elif score >= 50:
    print('D')
else:
    print ('F')

print()

#Here we have a person dictionary

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    if len(person['skills']) % 2 == 0:
        print(person['skills'][int(len(person['skills']) / 2 - 1):int(len(person['skills']) / 2 + 1)])
    else:
        print(person['skills'][int(len(person['skills']) / 2)])

else:
    print('Skills does not exist.')

print()


if 'skills' in person:
    if 'Python' in person['skills']:
        print('Yes there is Python.')
    else:
        print('No Python found.')
else:
    print('Skills does not exist.')

print()

skills_set = set(person['skills'])

if {'JavaScript', 'React'} == skills_set:
    print('He is a front end developer')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
    print('He is a backend developer')
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
    print('He is a fullstack developer')
else:
    print('unknown title')

print()

# * If the person is married and if he lives in Finland, print the information in the following format:


if person['is_marred'] and person['country'] == 'Finland':
    print('Yes')
else:
    print('No')


