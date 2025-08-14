#create a dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog = dict(name = "Milo", color = "black", breed = 'corgi', legs = 4, age = 3)
print(dog)
print()

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = dict(first_name = 'Nabz', last_name = 'Kebabz', gender = 'Male', age = 24, marital_status = 'single', skills = ['Python', 'Lifting'], country = 'Singapore', city = 'Singapore', address = 'Hougang')
print(student)
print()

#Get the length of the student dictionary
print('Length:',len(student))
print()

#Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
print()

#Modify the skills values by adding one or two skills
student['skills'].append('doomscrolling')
print(student['skills'])
print()

#Get the dictionary keys as a list
print(student.keys())
print()

#Get the dictionary values as a list
print(student.values())
print()

#Change the dictionary to a list of tuples using items() method
student = list(student.items())
print(student)
print()

#Delete one of the items in the dictionary
student = dict(student)
print(student)
del student['city']
print(student)
print()

#del dictionary
del student
print(student)