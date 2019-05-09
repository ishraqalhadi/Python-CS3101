while balance < 1000:
    interest = balance * 6/100.0	# use 100.0 to ensure float division
    balance = balance + interest    
    years = years + 1

print "It will take", years, "years for your investment to reach £1000"
