INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, len(graph)):
        graph[i][i] = 0

    for fare in fares:
        node1, node2, cost = fare
        graph[node1][node2] = cost
        graph[node2][node1] = cost

    for node in range(1, n + 1):
        for i in range(1, len(graph)):
            for j in range(1, len(graph[0])):
                graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])

    answer = graph[s][a] + graph[s][b]
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
          [1, 6, 25]])  # 82
