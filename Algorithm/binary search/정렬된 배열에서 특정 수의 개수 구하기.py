from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
array = list(map(int, input().split()))

print(bisect_right(array, m) - bisect_left(array, m))
