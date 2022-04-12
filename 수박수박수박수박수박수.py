def solution(n):
    answer = ''
    temp_lsit = ['박', '수']
    
    for i in range(1,n+1):
        answer += temp_lsit[i%2]
    return answer