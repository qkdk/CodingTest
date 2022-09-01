import heapq

q = []

heapq.heappush(q, (1, 'a'))
heapq.heappush(q, (2, 'a'))
heapq.heappush(q, (3, 'a'))
heapq.heappush(q, (4, 'a'))
heapq.heappush(q, (5, 'a'))
heapq.heappush(q, (3, 'a'))

print(q)
