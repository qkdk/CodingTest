def solution(n, left, right):
    answer = []
    lefte = left % n
    for i in range(left // n + 1, right // n + 2):
        for j in range(1, i):
            answer.append(i)
        for k in range(i, n + 1):
            answer.append(k)

    answer = answer[lefte:]
    answer = answer[:right - left + 1]
    return answer


solution(3, 2, 5)
solution(4, 7, 14)
# 123 223 333
