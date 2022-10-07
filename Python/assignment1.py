x = 10
y = 20 
print ("Before swapping: ")
print("Value of x is ", x, " and y is ", y)
x = x + y
y = x - y 
x = x - y
print ("After swapping: ")
print("Value of x is ", x, " and y is ", y)

Total_apples = 100
print ("Total_apples is ",Total_apples)
CP_of_1apple = 7.5
print ("CP_of_1apples is ",CP_of_1apple)
CP_of_100apples = Total_apples*CP_of_1apple
print ("CP_of_100apples is ",CP_of_100apples)
CP_of_50apples = CP_of_100apples/2
print ("CP_of_50apples is ",CP_of_50apples)
first_selling_quantity = 20
first_selling_PriceEach = 10
first_selling_Price = first_selling_quantity*first_selling_PriceEach
second_selling_quantity = 30
second_selling_PriceEach = 50
second_selling_Price = second_selling_quantity*second_selling_PriceEach
SP_of_50apples = first_selling_Price + second_selling_Price
print ("SP_of_50apples is ",SP_of_50apples)
profit_or_loss = SP_of_50apples - CP_of_50apples
print ("profit_or_loss is ",profit_or_loss)
apples_purchased_with_earnedAmount = SP_of_50apples//CP_of_1apple
print ("apples can be purchased with earned amount is ",apples_purchased_with_earnedAmount)
