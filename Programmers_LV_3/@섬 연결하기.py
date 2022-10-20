def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, node1, node2):
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2

    return parent


def solution(n, costs):
    answer = 0
    parent = [x for x in range(n)]
    costs.sort(key=lambda x: -x[2])

    while costs:
        node1, node2, cost = costs.pop()
        parent1 = find_parent(parent, node1)
        parent2 = find_parent(parent, node2)

        if parent1 != parent2:
            parent = union_parent(parent, parent1, parent2)
            answer += cost

    return answer


# solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])
# solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]])
solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])
