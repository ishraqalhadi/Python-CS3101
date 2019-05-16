#increase the prices by 20%
for i in range(4):
    priceIncrease = priceOf[i] * 20/100.0
    priceOf[i] = priceOf[i] + priceIncrease

# display the new prices
print
print "%15s%15s%20s" %("Item No", "Item", "Item Price") 
for i in range(4):
    print "%15d%15s%20.2f" %(i+1,food[i],priceOf[i])
