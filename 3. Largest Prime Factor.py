def main():
	k = 600851475143
	a = 0
	for x in range(3, int(k ** 0.5) + 1, 2):
		if k % x == 0:
			for y in range(3, int(x ** 0.5) + 1, 2):
				if x % y == 0:
					break
			else:
				a = x
	print(a)


main()
