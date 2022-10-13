import heapq


def solution(N, road, K):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for i in road:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))

    heap = []
    distance[1] = 0
    heapq.heappush(heap, (1, 0))

    while heap:
        node, dist = heapq.heappop(heap)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (i[0], cost))

    for i in distance:
        if i <= K:
            answer += 1

    return answer


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
