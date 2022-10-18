from collections import deque


def solution(n, computers):
    dp = [0 for _ in range(n)]

    network = [[] for _ in range(n)]
    for node in range(len(computers)):
        network[node].append(node)
        tmp = []
        for i in range(len(computers[node])):
            if node == i:
                continue
            if computers[node][i] == 1:
                tmp.append(i)
        network[node].append(tmp)

    count = 0
    for x in range(n):
        if dp[x] == 1:
            continue
        count += 1
        q = deque()
        q.append(network[x])
        while q:
            node, arr = q.popleft()

            dp[node] = 1

            for i in arr:
                if dp[i] == 0:
                    q.append(network[i])

    return count


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])

'''
좌표(index로 표햔)와 연결 되어있는 좌표를 리스트에 표시 [3,4,6,8...]
bfs 를 실시하고 q.pop 할때마다 해당 좌표 파악
'''
