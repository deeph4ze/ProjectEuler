#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

=begin
def is_satisfactory(x)
	for y in 1..20
		if x % y == 0
			next
		else 
			return false
			break
		end
	end
	return true
end


n = 1

until is_satisfactory(n)
	n += 1
	puts n
end
=end
i = 1
while true
  break unless (11..20).any? {|d| i % d != 0}
  i+=1
end
puts i
