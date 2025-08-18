#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num_1, num_2):
    return num_1 + num_2

print(add_two_numbers(10, 15))
print()

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return 3.14 * radius ** 2

print(area_of_circle(10))
print()

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
#Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    sum = 0
    for arg in args:
        if isinstance(arg, int):
            sum = sum + arg
        else:
            raise TypeError('Argument is not a string')

print(add_all_nums(1,2,3))
#print(add_all_nums(1,2,'three'))
print()

#Declare a function named evens_and_odds . 
#It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    even_list = []
    odd_list = []

    if number > 0 and isinstance(number, int):
        for i in range(1, number+1):
            if i % 2 == 0:
                even_list.append(i)
            else:
                odd_list.append(i)
    else:
        raise ValueError('Number must be a positive integer')

    even_count = len(even_list)
    odd_count = len(odd_list)

    return f'The number of odds are {odd_count}.\nThe number of evens are {even_count}.'

print(evens_and_odds(100))
print()

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    result = 1
    if number > 0 and isinstance(number, int):
        for i in range (number, 0, -1):
            result = result * i
    else:
        raise ValueError('Number must be a positive integer.')
    
    return result

print(factorial(5))
print()

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(variable):
    if variable:
        return False
    else:
        return True

print(is_empty([]))        # Should return True (empty list)
print(is_empty(""))        # Should return True (empty string) 
print(is_empty([1, 2, 3])) # Should return False (not empty)
print(is_empty("hello"))   # Should return False (not empty)
print(is_empty(0))         # Should return True (falsy value)
print(is_empty(None))      # Should return True (None is empty)

print()

#Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if number > 0 and isinstance(number, int):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        raise ValueError('must be positive int')

print(is_prime(5))




