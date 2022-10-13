from copy import deepcopy


def solution(land):
    dp = deepcopy(land)

    for i in range(len(land)):
        for j in range(len(land[0])):
            for k in range(len(land[0])):
                if k == j:
                    continue
                dx, dy = k, i - 1
                if dy < 0 or dy >= len(land):
                    continue
                if land[i][j] + dp[dy][dx] > dp[i][j]:
                    dp[i][j] = land[i][j] + dp[dy][dx]

    answer = max(dp[-1])
    return answer


solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])
