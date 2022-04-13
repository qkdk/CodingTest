def solution(n):
    n = int(n)
    temp_list = [int(x) for x in str(n)]
    temp_list.sort()
    answer =''
    for i in range(len(str(n))):
        answer += str(temp_list.pop())
    
    return int(answer)

solution(3771)