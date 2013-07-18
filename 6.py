squareOfSum = 0
sumOfSquare = 0
for x in range(1, 101):
	squareOfSum += x

squareOfSum = squareOfSum**2

for x in range (1, 101):
	sumOfSquare += x**2

print "The answer is: %s" % (sumOfSquare-squareOfSum	)