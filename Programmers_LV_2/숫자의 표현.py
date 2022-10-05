def solution(n):
    answer = 1

    # 반복
    for i in range(2, n):
        # 등차수열 합 계산
        sum = cal_sum(i)
        if sum >= n:
            break

        if (n - sum) % i == 0:
            answer += 1

    print(answer)

    return answer


def cal_sum(n):
    return (n - 1) * n / 2


solution(15)
