def solution(n):
    a= str(n)
    return [int(a[-x]) for x in range(1,len(a)+1)]

solution(12345)