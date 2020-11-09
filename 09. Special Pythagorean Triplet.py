def main():
	for a in range(1, 999):
		for b in range(1, 999 - a):
			if 2e3 * (a + b) - 2 * a * b == 1e6:
				print(a * b * (1000 - a - b))
				exit(0)


main()
