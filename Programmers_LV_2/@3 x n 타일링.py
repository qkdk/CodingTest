def solution(n):
    dp = [0] * (n + 1)

    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    dp[4] = 11

    for i in range(6, n + 1, 2):
        dp[i] = 4 * dp[i - 2] - dp[i - 4]

    return dp[-1] % 1000000007


solution(24)
