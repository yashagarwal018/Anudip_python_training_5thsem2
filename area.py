'''import math
s1 = int(input("enter the 1st side"))
s2 = int(input("enter the 2nd side"))
s3 = int(input("enter the 3rd side"))+++++
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
print("Perimeter =",perimeter,"cm")'''
#selection construct
#it takes condition and depending on result of condition statement gets executed
#problem to input time in sec
#and convert into corresponding hours minute second
#a funtion to execute to terminate or exit the program in python
#To calculate 
# to execute the task when condition is true in IF statement
#syntax if(condition):
#          statement/task
'''second = int(input("time input in seconds"))
#if second is negative 
if(second<0):
    exit("time cannot be negative")
print("..........................")
hours = 0
minutes = 0
#converting number of second in hours 
if(second>3600):
    hours = second//3600
    second = second%3600
#..........................................
#converting into minute 
if(second>=60):
    minute = second//60
    second = second%60
print(hours,minute,second)'''
#To calculate the simple interest
principle = int(input("enter the principle amount"))
Rate = int(input("enter the Rate amount"))
Time = int(input("enter the Time amount"))
if(principle<0):
    exit("not negative")
if(principle<0):
    exit("not negative")
if(Rate<0):
    exit("not negative")
if(Time<0):
    exit("not negative")
simpleinterest = (principle*Rate*Time)/100
print(simpleinterest)
