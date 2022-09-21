from collections import deque


def solution(priorities, location):
    q = deque([])
    lst = []
    for i in range(len(priorities)):
        q.append({i: priorities[i]})

    print(q)
    while q:
        tmp = q[0]
        q.popleft()
        length = len(q)
        flag = False
        for i in range(length):
            if list(tmp.values())[0] < list(q[i].values())[0]:
                flag = True

        if flag:
            q.append(tmp)
        else:
            lst.append(list(tmp.keys())[0])

    for i in range(len(lst)):
        if lst[i] == location:
            return i + 1


solution([2, 1, 3, 2], 2)
