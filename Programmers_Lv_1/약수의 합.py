def solution(n):
    answer = 0
    numlist= []
    for i in range(1,n+1):
        if n%i == 0:
            numlist.append(i)
    
    answer = sum(numlist)
    return answer

#계산하는 수를 2로 나누어서 하면 계산시간 2배 향상