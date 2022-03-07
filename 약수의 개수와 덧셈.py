import math

def solution(left, right):
    answer = 0

    for i in range(left,right+1):
        rt = i**(1/2)
        crt = math.ceil(rt)
        if crt - rt > 0:
            answer += i
        else:
            answer -= i
    
    print(answer)
    return answer

solution(13, 17)