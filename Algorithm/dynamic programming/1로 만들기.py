'''
1 => 1
2 => /2
3 => /3
4 => /2 -1 or -1 /3
5 => /5
6 => /2 /3 or /3 /2
.
.
.
26 => -1 => 25의 최소횟수 +1
27 => /3 => 9의 최소횟수 +1

2의 배수 일 경우 2로 나누고
3의 배수 일 경우 3으로 나누고
5의 배수 일 경우 5로 나누고
안되는 경우 1을 빼서 나눌수 있는 값을 찾는다.

dp[n] = min(dp[n-1] , dp[n/2], dp[n/3], dp[n/5]) + 1
'''

n = int(input())

dp = [0] * (n + 1)
minValue = [n] * 4

for i in range(2, n + 1):
    if i % 2 == 0:
        minValue[0] = dp[i // 2]
    if i % 3 == 0:
        minValue[1] = dp[i // 3]
    if i % 5 == 0:
        minValue[2] = dp[i // 5]
    minValue[3] = dp[i - 1]

    dp[i] = min(minValue) + 1
    minValue = [n] * 4

print(dp[n])
