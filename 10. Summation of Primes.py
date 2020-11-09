def main():
	primes = [2]
	x = 3

	while primes[-1] <= 2e6:
		for p in primes:
			if x % p == 0:
				break
			if p * p > x:
				primes.append(x)
				break
		# else:
		# 	primes.append(x)

		x += 1
	print(sum(primes[:-1]))


main()
