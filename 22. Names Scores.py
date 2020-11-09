def main():
	with open('22. Input.txt', 'r') as f:
		names = sorted(f.read().replace('"', '').split(','))

	a = 0
	for i, name in enumerate(names):
		a += (i + 1) * sum(ord(x) - 64 for x in name)

	print(a)


main()
