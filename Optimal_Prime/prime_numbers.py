prime_numbers = list(range(1,1000))
prime_numbers.remove(1)
for count in prime_numbers:
	for x in range(2,len(prime_numbers)):
		remover = x * count
		if remover in prime_numbers:
			prime_numbers.remove(remover)
print(prime_numbers)
print(len(prime_numbers))