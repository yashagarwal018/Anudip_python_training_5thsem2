import math
s1 = int(input("enter the 1st side"))
s2 = int(input("enter the 2nd side"))
s3 = int(input("enter the 3rd side"))
print("................................")
print("1st side",s1,"cm")
print("2nd side",s2,"cm")
print("3rd side",s3,"cm")
#Calculate the perimeter 
perimeter = s1+s2+s3
s=perimeter/2
#Calculate the area 
#area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
#display the area 
print("Area =",(s*(s-s1)*(s-s2)*(s-s3))**0.5,"sq.cm")
#display the perimeter
print("Perimeter =",perimeter,"cm")