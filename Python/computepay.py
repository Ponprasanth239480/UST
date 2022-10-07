def computepay(hours,rate):
    return total


hours = int(input("enter the toatal working hours"))
rate = int(input("enter the working rate per hour"))

if (hours > 40):
    totalrate = 40*rate + (hours-40)*1.5*rate
else:
    totalrate = hours *rate
    

