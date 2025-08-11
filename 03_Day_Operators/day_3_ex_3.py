#Get length and width of a rectangle using prompt. 
#Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter Length: "))
width  = int(input("Enter Width: "))

perimeter = 2 * (length + width)
area = length * width

print("perimeter: ", perimeter, "\n"
      "area: ", area, "\n")
