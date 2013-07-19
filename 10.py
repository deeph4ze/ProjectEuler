#
# Summation of all primes below 2 million
#
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

def summate_primes(n):
 	total = 0
 	for i in range(1, n+1):
 		if(is_prime(i)):
 			total += i
 			print i
 		else:
 			continue
 	return total

print summate_primes(2000000)
now = time.time()-start
print "Found in %s seconds" % now
