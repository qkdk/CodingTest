import heapq


def solution(n, works):
    answer = 0
    heapq.heapify(works)

    q = []
    for i in works:
        heapq.heappush(q, -i)

    for _ in range(n):
        heapq.heappush(q, heapq.heappop(q) + 1)

    for i in q:
        answer += i ** 2

    if q[-1] > 0:
        return 0
    
    return answer


# solution(4, [4, 3, 3])
# solution(1, [2, 1, 2])
solution(3, [1, 1])
