#PROBLEM 4A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(thing)
	if thing.to_s == thing.to_s.reverse
		return true
	else return false
	end
end
x = 999
y = 999
list = []

while x > 900
	while y > 0 
		if is_palindrome(x*y)
			list.push(x*y)
			y -= 1
		else
			y -= 1
		end
	end
	x -= 1
	y = 999
end

puts list.sort.last

