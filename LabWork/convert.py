second = int(input("time input in seconds"))
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
print(hours,minute,second)
