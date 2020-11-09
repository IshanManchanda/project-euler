def main():
	n = 1
	while True:
		a = n * (n + 1) // 2

		d = 0
		for x in range(1, a + 1):
			if a % x == 0:
				if x * x == a:
					d += 1
				else:
					d += 2
			if x * x >= a:
				break

		if d > 500:
			print(a)
			exit(0)

		n += 1


main()
