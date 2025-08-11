#Get radius of a circle using prompt. 
#Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14

radius = float(input("Enter Radius: "))
area = round(pi * radius ** 2, 2)
circumference = round(2 * pi * radius, 2)

print("area: ", area, "\n"
      "circumference: ", circumference)