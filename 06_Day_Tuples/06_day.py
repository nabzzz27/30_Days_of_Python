#Create an empty tuple
empty_tuple = tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
#join them
main_c = ('Spongebob', 'Patrick', 'Squidward')
side_c = ('Mr Krabs', 'Sandy')
print(main_c + side_c)
print()

#How many siblings do you have?
print(len(main_c + side_c))
print()

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
characters = (main_c + side_c) + ('Plankton', 'Larry')
print(characters)
print()

#Unpack siblings and parents from family_members
main_1, best_f, neighbour, *support = characters
print(main_1, best_f, neighbour, tuple(support))
print()

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Banana')
vegetables = ('Lettuce', 'Cucumber')
animal_products = ('Kibble', 'Pads')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
print()

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print()

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_tp) % 2 == 0:
    print(food_stuff_tp[int(len(food_stuff_tp) / 2) - 1 : int(len(food_stuff_tp) / 2) + 1])
else:
    print(food_stuff_tp[int(len(food_stuff_tp)//2) + 1])

#Slice out the first three items and the last three items from food_staff_lt list
print()
print(food_stuff_lt[:3] + food_stuff_lt[-3:])
del food_stuff_tp

#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
