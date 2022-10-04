import math


def solution(n, k):
    num = [x for x in range(1, n + 1)]
    stack_facto = [math.factorial(x) for x in range(n - 1, 0, -1)]
    stack_div = []
    answer = []

    k -= 1
    for facto in stack_facto:
        stack_div.append(k // facto)
        k = k % facto

    for i in stack_div:
        answer.append(num[i])
        num.pop(i)

    answer.extend(num)

    return answer


solution(3, 5)
# solution(4, 22)

# 3 -> 4 -> 5
# 2 -> 6 -> 24
