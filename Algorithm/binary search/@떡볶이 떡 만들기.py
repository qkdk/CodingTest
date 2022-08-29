n, m = map(int, input().split())
riceCake = list(map(int, input().split()))

start, end, mid = 0, max(riceCake), max(riceCake) // 2
answer = ''
while start < end:
    mid = (start + end) // 2

    result = sum([x - mid for x in riceCake if x - mid > 0])

    if result < m:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)
