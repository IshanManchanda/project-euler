def is_pal(n):
	return str(n) == str(n)[::-1]


def main():
	a = []
	for i in range(999, 900, -1):
		for j in range(999, 900, -1):
			if is_pal(i * j):
				a.append(i * j)
	print(max(a))


main()
