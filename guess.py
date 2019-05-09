print "Guess the mystery number - it's between 1 and 100!"
guess = input("Type in your first guess: ")
while guess != number:
    if guess > number:
        print "Too high! Guess lower!"
    else:
        print "Too low! Guess higher!"
    guess = input("Type in your guess:")

print "Well done. You are right!"
print "The number was", number
