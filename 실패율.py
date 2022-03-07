import collections

def solution(N, stages):
    answer = []

    user = len(stages)
    dic_stages = collections.Counter(stages)
    list_fail = []
    cur_N = user

    for i in range(1, N + 1):
        if cur_N == 0:
            list_fail.append(0.0)
        else:
            list_fail.append(dic_stages[i]/cur_N)
            cur_N -= dic_stages[i]

    for i in range(N):
        answer.append(list_fail.index(max(list_fail)) + 1)
        list_fail[list_fail.index(max(list_fail))] = -1
    
    print(answer)
    return answer
