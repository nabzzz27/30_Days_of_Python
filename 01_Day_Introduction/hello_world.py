print('Hello World!')

print("===================\n")
print('Addition:', 5 + 4) #addition
print('Subtraction:', 5 - 4) #subtraction
print('Division:', 5 / 4) #division
print('Multiplication:', 5 * 4) #multiplication
print('Modulus:', 5 % 4) #remainder
print('Floor:', 5 // 2) #floor
print ('Exponent:', 5 ** 4) #power

print("===================\n")
print('Integer:',type(1)) #int
print('Float:', type(1.0)) #float
print('Complex:', type(1 + 3j)) #complex
print('String:', type('Nabil')) #str
print('List:', type(['Batman', 1, True])) #list
print(type({'name' : 'nabil', 
       'age' : 24,
       'height (cm)' : 183.0})) #dict
print(type((1,2,3))) #list, immutable 
print(type(True)) #bool

####################################
#Exercise 3
#Find Euclidean Distance between (2,3) and (10,8)
#formula sqrt((x1-x2)**2 + (y1-y2)**2)
print("===================\n")
euc_dist=((2 - 10)**2 + (3 - 8)**2)**0.5
print('Distance:', round(euc_dist, 2)) #built in round function to round it to 2 decimal places
print(type(euc_dist))