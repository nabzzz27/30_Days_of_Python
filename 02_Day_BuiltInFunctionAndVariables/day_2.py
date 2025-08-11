#Day 2 of 30 days of python, Built in Functions and Variables
#python has a number of built in functions eg len(), float(), str()
#exercise 1
first_name = 'Nabil'
last_name = 'Zafran'
full_name = 'Nabil Zafran'
country = 'Singapore'
city = 'Singapore'
age = 24
year = 2025
is_married = False
is_true = False
is_light_on = True
hero, height, vehicle = 'Batman', 190, {'car':'batmobile'}
print(hero, height, vehicle)

#exercise 2
print('======================')
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(hero), type(height), type(vehicle))

print(len(first_name))
print(len(first_name) - len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_two % num_one
print(remainder)
exp = num_one ** num_two
print(exp)
floor_division = num_one // num_two
print(floor_division)

r = 30
area_of_circle = (3.14)*r**2
circum_of_circle = (3.14)*2*r
print(area_of_circle, circum_of_circle)

radius = int(input("input the radius of your circle: "))
area = (3.14)*radius**2
print("are of cirlce is ", area)