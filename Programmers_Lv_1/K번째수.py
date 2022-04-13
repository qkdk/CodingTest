def solution(array, commands):
    answer = []

    for x,y,z in commands:
        lst = array[x-1:y]
        lst.sort()
        answer.append(lst[z-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	
solution(array,commands)