dp = {1: 1}


def collatz(n):
	if n in dp:
		return dp[n]

	if n % 2 == 0:
		dp[n] = collatz(n // 2) + 1
	else:
		dp[n] = collatz(3 * n + 1) + 1

	return dp[n]


def main():
	m, mc = 1, 1
	for x in range(1, 1000001):
		c = collatz(x)
		if c > mc:
			m, mc = x, c

	print(m)


main()
