def solution(n, s):
    answer = []

    flag = s // n
    remain = s - flag * n

    if flag < 1:
        return [-1]

    for _ in range(n):
        if remain > 0:
            answer.append(flag + 1)
            remain -= 1
        else:
            answer.append(flag)

    answer.sort(reverse=False)

    return answer


solution(2, 9)
