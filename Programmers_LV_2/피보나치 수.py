def solution(n):
    answer = []
    answer.append(1)
    answer.append(1)

    for i in range(2, n):
        answer.append(answer[i - 2] + answer[i - 1])

    return answer[n - 1] % 1234567


solution(3)
