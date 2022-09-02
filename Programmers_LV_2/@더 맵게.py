import heapq


def solution(scoville, K):
    answer = 0
    q = []

    for i in scoville:
        heapq.heappush(q, i)

    while q[0] < K:
        if len(q) < 2:
            answer = -1
            break
        first_char = heapq.heappop(q)
        heapq.heappush(q, first_char + heapq.heappop(q) * 2)
        answer += 1

    return answer
