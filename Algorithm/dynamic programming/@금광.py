for _ in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    for i in range(1, m):
        for j in range(n):
            if j == 0:
                leftUp = 0
            else:
                leftUp = dp[j - 1][i - 1]
            if j == n - 1:
                leftDown = 0
            else:
                leftDown = dp[j + 1][i - 1]
            left = dp[j][i - 1]
            dp[j][i] += max(left, leftDown, leftUp)

    temp = 0
    for i in range(n):
        temp = max(temp, dp[i][-1])

    print(temp)
