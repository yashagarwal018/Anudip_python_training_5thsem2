#To calculate the simple interest
principle = int(input("enter the principle amount"))
if(principle<0):
    exit("not negative")
Rate = int(input("enter the Rate amount"))
if(Rate<0):
    exit("not negative")
Time = int(input("enter the Time amount"))
if(Time<0):
    exit("not negative")
simpleinterest = (principle*Rate*Time)/100
print(simpleinterest)
