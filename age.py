print "This program tells you if you are of working age"
print

age = input("Type in your age:  ")
print 

if age > 16  and age < 65:
    print "You are of working age"
else:
    print "You are not of working age"
print "Goodbye"
print "This program will calculate if you are "
print "in the age range to qualify for Jury Service"
print

age = input("How old are you: ")

if age < 18 or age >= 70:
    print "You do not qualify for Jury Service."
    print "You have to be at least 18 years old and under 70"
    print "years old to serve on a Jury."
else:
    print "You are qualified for Jury Service"
    print "as you are at least 18 years old and under"
    print "70 years old."
