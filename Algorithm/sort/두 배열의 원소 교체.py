n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))
