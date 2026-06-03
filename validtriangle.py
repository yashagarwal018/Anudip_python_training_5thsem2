side1 = float(input("Enter the first side"))
if(side1<=0):
    exit("not negative")
#wap to check 3 sides forms a triangle or not 
side2 = float(input("Enter the second side "))
if(side2<=0):
    exit("not negative")
side3 = float(input("Enter the third side"))
if(side3<=0):
    exit("not negative")
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("triangle is form")
else:
    print("triangle")