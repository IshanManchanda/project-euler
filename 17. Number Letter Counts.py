def main():
	single_digit = 36
	teens = 70
	second_digit = 46
	hundred = 7
	nd = 3
	thousand = 11

	a = single_digit * (10 * 19)
	a += second_digit * 10 * 10
	a += teens * 10
	a += hundred * 900
	a += nd * 891
	a += thousand

	print(a)


main()
