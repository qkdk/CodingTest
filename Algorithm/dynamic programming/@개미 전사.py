n = int(input())
array = list(map(int, input().split()))

# 점화식 계산하기
# arrayMax[n] = MAX( arrayMax[n-1], arrayMax[n-2] + array[i])

# arrayMax = dpTable
dp = [0] * n

dp[0] = array[0]
dp[1] = max(array[1], array[2])

for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[n - 1])
