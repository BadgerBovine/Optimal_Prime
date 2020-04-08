prime_numbers = list()
for num in range(0,1000):
	for i in range(2,num):
		if (num % i) != 0:
			prime_numbers.append(num)
print(prime_numbers)
print(len(prime_numbers))