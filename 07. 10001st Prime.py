def main():

	primes = [2]
	x = 3
	while len(primes) < 10001:
		for p in primes:
			if x % p == 0:
				break
			if p * p > x:
				primes.append(x)
				break
		x += 1
	print(primes[-1])


main()
