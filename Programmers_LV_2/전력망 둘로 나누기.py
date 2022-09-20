from collections import defaultdict, deque
from itertools import combinations


def solution(n, wires):
    q = deque([])
    min_gap = n

    pos_wires = list(combinations(wires, len(wires) - 1))

    while pos_wires:
        cur_wires = pos_wires[-1]
        pos_wires.pop()
        info = defaultdict(list)
        visited_node = [False] * (n + 1)
        count_list = []

        for i in cur_wires:
            info[i[0]].append(i[1])
            info[i[1]].append(i[0])

        # print(info)
        for i in range(1, n + 1):
            if visited_node[i]:
                continue

            count = 1
            visited_node[i] = True
            q.extend(info[i])

            while q:
                node = q.popleft()
                if not visited_node[node]:
                    count += 1
                    visited_node[node] = True
                    q.extend(info[node])

            if count != 0:
                count_list.append(count)

        di = abs(count_list[0] - count_list[1])
        if min_gap > di:
            min_gap = di

    return min_gap


solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
