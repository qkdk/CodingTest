n = int(input())

stair = []
dp = []

for i in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])

elif n == 2:
    print(stair[0] + stair[1])

else:
    dp.append(stair[0])
    dp.append(stair[0] + stair[1])
    dp.append(max(stair[2] + stair[1], stair[0] + stair[2]))

    for i in range(3,n):
        dp.append(max(stair[i] + stair[i-1] + dp[i-3], dp[i-2] + stair[i] ))
    
    print(dp[n-1])