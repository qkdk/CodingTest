def solution(d, budget):
    
    d.sort()
    answer = 0
    sum = 0

    for i in d:
        sum += i
        if sum > budget:
            break
        answer += 1

    return answer

solution([1, 3, 2, 5, 4], 9)