from collections import deque


def solution(n, t, m, p):
    q = deque()

    answer = ''

    number = 0
    for i in range(t * m):
        # print(make_number(i, n))
        if len(q) == 0:
            q.extend(make_number(number, n))
            number += 1

        if i % m == p - 1:
            answer = answer + q[0]

        q.popleft()

    print(answer)
    return answer


def make_number(number, n):
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    q = deque()

    while number >= n:
        tmp = number % n
        if tmp in dic.keys():
            tmp = dic[tmp]

        q.appendleft(str(tmp))
        number = number // n

    if number in dic:
        number = dic[number]

    q.appendleft(str(number))

    return q


solution(16, 16, 2, 1)
