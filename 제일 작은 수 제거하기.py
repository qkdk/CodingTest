def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))
    answer = arr
    if len(arr) == 0:
        answer = [-1]
    
    return answer