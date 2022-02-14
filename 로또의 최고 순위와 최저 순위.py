def solution(lottos, win_nums):

    rank = [6,6,5,4,3,2,1]
    ct = 0
    
    for i in lottos:
        if i in win_nums:
            ct += 1
    
    zc = lottos.count(0)
     
    answer = [rank[ct+zc], rank[ct]]
    return answer