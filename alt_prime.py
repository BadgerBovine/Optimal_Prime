target = 700000
t50 = int(target/2)
t33 = int(target/3)
prime_numbers = list(range(2,target))
remover = list()
for x in range(2,t50):
	nprime = x * 2
	if nprime < target:
		remover.append(nprime)
for count in range(3,t33+1,2):
	lim = target / count
	lim = int(lim)
	for x in range(count,lim+1,2):
		if x <= lim:
			nprime = x * count
			if nprime < target:
				remover.append(nprime)
remover.sort()
length = len(remover)
for i in range(length,0,-1):
	bol = remover[i-2] != remover[i-1]
	if remover[i-2] != remover[i-1]:
		idex = remover[i-1]-2
#		print(idex)
#		print(len(remover))
		del prime_numbers[idex]
print(prime_numbers)
print(len(prime_numbers))