def main():
	d = [0, 0]
	a = 0

	for x in range(2, 10001):
		d.append(1)
		for y in range(2, x + 1):
			if x % y == 0:
				if y * y == x:
					d[x] += y
				else:
					d[x] += y + x // y
			if y * y >= x:
				break

	for i in range(2, 10001):
		if d[i] != i and d[i] < 10001 and d[d[i]] == i:
			a += i

	print(a)


main()
