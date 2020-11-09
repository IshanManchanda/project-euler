def main():
	k = 600851475143
	a = 0
	for x in range(3, k // 2 + 1, 2):
		if k % x == 0:
			for y in range(3, x, 2):
				if x % y == 0:
					break
				if y * y > x:
					a = x
					break
	print(a)


main()
