def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)
        
        answer.sort()

    if answer == []:
        answer = [-1]
    return answer

solution([5, 9, 7, 10],5)