"""# 1 
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("the number is even")
else:
    print("the number is even")


#2

fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit_value - 32) * 5/9
print(f"{fahrenheit_value} in Fahrenheit is equal to {celsius} in Celsius")
celsius_value = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius_value} in celsius is equal to {fahrenheit} in fahrenheit")


#3

inches = float(input("Enter the value in inches:"))
centimeters = inches * 2.54
print(inches,'Inches =', centimeters,'Centimeters')
meters = inches // 39.37
cm = (inches%39.37)*2.54
print(inches,'Inches =', int(meters),'meters  and  ', int(cm),'centimeters')


#4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#5

num = int(input("Enter the number: "))
reversed_num = 0

while num != 0:
    lastdigit = num % 10
    reversed_num = reversed_num * 10 + lastdigit
    num //= 10

print("Reversed Number: " + str(reversed_num))

"""

#6
num = int(input("Enter a number: "))

if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")



#7

lower = int(input("Enter a lower_limit: "))
upper = int(input("Enter a upper_limit: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


