Amount=100
print ("original amount", Amount)
Amount +=20
print ("amount with additional 20 voucher", Amount)
Amount -=15
print ("amount remaining after spending 15rs", Amount)
Amount *=2
print ("amount remaining after jackpot", Amount)
Amount /=2
print ("amount remaining after dividing between 2", Amount)
number_of_icecreams = Amount//25
amount_remaining = Amount%25
print ("amount remaining after purchasing", number_of_icecreams,"icecream in rupees",amount_remaining)
Amount = amount_remaining**5
print ("amount remaining after jackpot", Amount)
