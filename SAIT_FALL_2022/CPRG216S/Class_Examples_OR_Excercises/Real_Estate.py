
CPrice = int(input("Enter Current Price:"))
LMPrice = int(input("Enter Last Months Price: "))

Price_Change = CPrice - LMPrice 
EMorgage = (CPrice * 0.051) / 12 

print("Current Price:" , CPrice)
print("Change Since Last Month" , Price_Change)
print("Estimated Monethly Morgage" , EMorgage)