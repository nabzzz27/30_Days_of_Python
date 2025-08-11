#Write a Python script that displays the following table
'''1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125'''

#5 rows and 5 columns

for i in range(1,6):
    print(i, end = "")
    for exponent in range (0,4):    
        print("", i ** exponent, end = "")
    print()
        