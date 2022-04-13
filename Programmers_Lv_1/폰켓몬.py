def solution(nums):
    answer = 0
    
    s_nums = set(nums)
    answer = len(s_nums)
    if len(nums)/2 < answer:
        answer = len(nums)/2

    return answer

solution([3,1,2,3])