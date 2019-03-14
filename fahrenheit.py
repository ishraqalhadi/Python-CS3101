print "This program will ask you to input the temperature in degrees Fahrenheit"
print "then output the equivalent temperature in degrees Centigrade."
print "The program will issue appropriate weather warnings for extreme"
print "temperatures."
print
fahrenheit = input ("Enter the temperature in degrees Fahrenheit: ")
centigrade =  (fahrenheit - 32)* 5/9.0
print "The equivalent temperature in degrees Centigrade is %0.0f" % centigrade
print

# check if weather warning needed
if centigrade <= 0:
    print "It's freezing. Best to wear a thick coat today."
elif centigrade > 30:
    print "It's hot, stay in the shade."
else:
    print "There are no extreme weather warnings today."
print "Have a pleasant day."
