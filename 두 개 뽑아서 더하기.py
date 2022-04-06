def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    result = list(set(answer))
    result.sort()
    print(result)
    return result

solution([2,1,3,4,1])