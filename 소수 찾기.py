import math

def solution(n):   
    num_list = [x for x in range(1,n+1)]
    num_list_answer = []

    temp1 = math.ceil(n**(1/2))
    for i in range(1,temp1):
        if num_list[i] != 0:
            num_list_answer.append(num_list[i])
            for j in range(i,n,num_list[i]):
                num_list[j] = 0 

    for k in range(n):
        if num_list[k] != 0:
            num_list_answer.append(num_list[k])
        
        answer = len(num_list_answer)-1
    return answer
    
# 아리스토테네스의 체 이용