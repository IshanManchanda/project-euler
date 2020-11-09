def main():
	primes = [2]
	x = 3

	while primes[-1] <= 2e6:
		for p in primes:
			if x % p == 0:
				break
		else:
			primes.append(x)

		x += 1

	print(sum(primes))


main()
