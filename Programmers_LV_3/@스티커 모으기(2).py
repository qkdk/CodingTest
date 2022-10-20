def solution(sticker):
    answer = []
    dp = [0] * len(sticker)

    if len(sticker) < 2:
        return max(sticker)

    # 두가지 케이스 존재
    # 첫번째를 뽑아서 마지막을 못 뽑는 경우
    # 마지막을 뽑아서 첫번째를 못 뽑는 경우
    dp[0] = sticker[0]
    dp[1] = max(dp[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer.append(dp[-2])

    sticker[0] = 0
    dp[0] = sticker[0]
    dp[1] = max(dp[0], sticker[1])
    for i in range(2, len(sticker)):
        dp[i] = max(dp[i - 2] + sticker[i], dp[i - 1])
    answer.append(dp[-1])

    answer = max(answer)

    return answer


solution([14, 6, 5, 11, 3, 9, 2, 10])
