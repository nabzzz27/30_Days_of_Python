import random
import string


#Write a function which generates a six digit/character random_user_id
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

# print(random_user_id())
# print()

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    user_id_list = []
    no_of_characters = int(input('Number of Desired Characters: '))
    no_of_ids = int(input('Number of Desired IDs: '))

    for i in range(no_of_ids):
        user_id =  ''.join(random.choice(characters) for i in range(no_of_characters))
        user_id_list.append(user_id)
    
    return '\n'.join(user_id_list)

#print(user_id_gen_by_user())
# print()

def rgb_color_gen():
    color_list = []

    for i in range(3):
        color = random.randint(0, 255)
        color_list.append(color)
    
    return tuple(color_list)

# print(rgb_color_gen())
# print()

def list_of_hexa_colors(number):
    hexadecimal_color_list = []
    characters = string.digits + 'abcdef'

    for i in range(number):
        hexadecimal_color = '#' + ''.join(random.choice(characters) for i in range(6))
        hexadecimal_color_list.append(hexadecimal_color)

    return hexadecimal_color_list

def list_of_rgb_colors(number):
    rgb_color_list = []
    for i in range(number):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_color_list.append(f"rgb({r}, {g}, {b})")
    return rgb_color_list



