from day_12 import list_of_hexa_colors, list_of_rgb_colors 

def generate_colors(string, number):
    if string == 'hexa':
        print(list_of_hexa_colors(number))
    elif string == 'rgb':
        print(list_of_rgb_colors(number))
    else:
        raise ValueError('type hexa or rgb then number')

generate_colors('hexa', 3)
generate_colors('rgb', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 1)
