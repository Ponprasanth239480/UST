
number_of_days = int(input("Enter number of days: "))
years = number_of_days // 365
months = (number_of_days - years *365) // 30
days = (number_of_days - years * 365 - months*30)

print(years,"Years ",months,"Months  ",days,"Days " )
