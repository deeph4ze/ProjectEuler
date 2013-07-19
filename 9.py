# pythagorean triplet  a < b < c where a**2 + b**2 = c**2
#
#find the only one for which a+b+c = 1000
#
#
#
import time

start = time.time()

def find_answer():
	for a in range(1, 998):
		for b in range(a+1,998):
			for c in range(b+1,998):
				if (a+b+c != 1000):
					continue
				else:
					if (a**2 + b**2 == c**2):
						print "final"
						print a
						print b
						print c
						now = time.time()-start
						print "found in" + str(now)
						return a*b*c
					else:
						print a
						print b
						print c
						continue

print find_answer()



