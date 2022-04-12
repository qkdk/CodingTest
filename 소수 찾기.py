def solution(n):
    answer = n-1
    
    for i in range(3,n+1):
        for j in range(2,i):
            if i%j == 0:
                answer -= 1
                break
              
    return answer

solution(10)