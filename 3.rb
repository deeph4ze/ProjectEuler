def is_prime(y)
	x = y - 1
	while x > 1
		if y % x == 0
			return false
		else
			x -= 1
		end
	end
	return true
end	

=begin

m = 40
while m % 2 == 0
	
	m = m/2
	puts m.to_s
end 

puts m
=end



n = 600851475143

m = 2

while m <= n
	if is_prime(m)
		while n % m == 0
			n = n/m
			puts n.to_s
			puts m.to_s
		end
		m += 1 
	else
		puts m.to_s
		m += 1
	end
end
