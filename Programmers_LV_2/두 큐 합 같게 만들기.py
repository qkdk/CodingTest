from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    count = 0
    while count < len(queue1) * 3:
        if sum_q1 == sum_q2:
            return count

        if sum_q1 > sum_q2:
            sum_q2 += q1[0]
            sum_q1 -= q1[0]
            q2.append(q1[0])
            q1.popleft()
            count += 1

        else:
            sum_q1 += q2[0]
            sum_q2 -= q2[0]
            q1.append(q2[0])
            q2.popleft()
            count += 1

    return -1


solution([1, 2, 1, 2], [1, 10, 1, 2])
