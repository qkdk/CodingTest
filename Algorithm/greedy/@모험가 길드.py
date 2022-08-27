n = int(input())
p = [int(x) for x in input().split()]

p.sort()
result = 0
groupCount = 0

for i in p:
    groupCount += 1
    if groupCount >= i:
        groupCount = 0
        result += 1

print(result)
