import heapq

INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 테이블 거리보다 멀다면 이미 방문한 노드라고 판단할 수 있다.
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m, c = map(int, input().split())
graph = [[] for x in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(c)

# 시작 노드 제외
count = -1
maxDistance = 0

for i in distance:
    if i != INF:
        count += 1
        maxDistance = max(i, maxDistance)

print(count, maxDistance)
