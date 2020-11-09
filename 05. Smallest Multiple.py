from math import gcd


def main():
	a = 1
	for i in range(1, 21):
		a = a * i // gcd(a, i)

	print(a)


main()
