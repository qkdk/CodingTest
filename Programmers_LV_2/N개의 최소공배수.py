import math


def solution(arr):
    a = arr[0]

    for i in range(1, len(arr)):
        b = arr[i]
        tmp = (a * b) / math.gcd(a, b)
        a = int(tmp)

    return a


solution([2, 6, 8, 14])
