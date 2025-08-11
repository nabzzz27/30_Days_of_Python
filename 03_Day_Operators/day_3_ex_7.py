#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = int(input('Enter Number of Hours you have worked: '))
rate = int(input('Enter your rate per hour: '))
print('Pay: $' + str(hours * rate))