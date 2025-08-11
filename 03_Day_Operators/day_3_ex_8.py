# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. 
# Assume a person can live hundred years

while True:
    age = int(input('Enter your age (less than 100): '))

    if age < 100:
        seconds = age * 365 * 24 * 60 * 60
        print('Number of seconds:' + str(seconds))
        break

    