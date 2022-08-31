MAX_NUMBER = 100000

n, k = map(int, input().split())

currency = []
dp = [MAX_NUMBER] * (k + 1)

for i in range(n):
    currency.append(int(input()))
    dp[currency[i]] = 1

for i in range(k + 1):
    for j in currency:
        if i - j >= 0:
            dp[i] = min(dp[i - j] + 1, dp[i])

if dp[-1] == MAX_NUMBER:
    print(-1)
else:
    print(dp[-1])
