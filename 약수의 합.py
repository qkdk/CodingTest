def solution(n):
    answer = 0
    numlist= []
    for i in range(1,n+1):
        if n%i == 0:
            numlist.append(i)
    
    answer = sum(numlist)
    return answer