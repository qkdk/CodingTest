import heapq


def solution(operations):
    heap = []

    for command in operations:
        c = command.split()
        if c[0] == 'I':
            heapq.heappush(heap, int(c[1]))
        else:
            if heap:
                if c[1] == '-1':
                    heapq.heappop(heap)
                else:
                    heap.remove(heapq.nlargest(1, heap)[-1])

    if heap:
        return [heapq.nlargest(1, heap)[-1], heapq.heappop(heap)]
    else:
        return [0, 0]


solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
