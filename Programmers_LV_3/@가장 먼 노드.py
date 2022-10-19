import heapq


def solution(n, edge):
    answer = 0
    INF = 50000
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    q = []
    heapq.heappush(q, (1, 0))
    distance[1] = 0

    while q:
        node, dist = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = 1 + dist
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (i, cost))

    max_value = max(distance[1:])
    for value in distance:
        if value == max_value:
            answer += 1

    return answer


# 다익스트라 알고리즘 사용
solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
