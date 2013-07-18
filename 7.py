#
#PROBLEM 7, find 10001st prime
#
import time
start = time.time()
def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True

count = 0
num = 1
while (count<10002):
	if (is_prime(num)):
		count += 1
		num += 1
		print count
	else:
		num += 1

print "FINAL ANSWER"
print count-1
print num
print time.time()-start




