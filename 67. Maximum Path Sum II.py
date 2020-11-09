def main():
	with open('67. Input.txt', 'r') as f:
		s = [[int(x) for x in y.strip().split()] for y in f.readlines()]

	for i in range(1, len(s)):
		s[i][0] += s[i - 1][0]
		s[i][-1] += s[i - 1][-1]

	for i in range(2, len(s)):
		for j in range(1, i):
			s[i][j] += max(s[i - 1][j - 1], s[i - 1][j])

	print(max(s[-1]))


main()
