#Huws Folly

primes = []

for i in range(100):
	prime = True
	for j in range(2, i):
		if not (i % j) == 0:
			prime = False
			break
			if prime:
				primes.append(i)
			
print(primes)