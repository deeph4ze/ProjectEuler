x = 1
y = 2
temp = 0
sum = 0



while y < 4000000
	if y % 2 == 0 
		sum = sum + y
		puts sum
	end

	temp = y
	y = x + y
	x = temp
	puts "y is #{y}"
end

puts "total is #{sum}"

