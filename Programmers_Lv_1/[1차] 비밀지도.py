def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        temp = format(arr1[i] | arr2[i], 'b')
        while len(temp)<n:
            temp = '0' + temp

        temp = temp.replace('1','#')
        temp = temp.replace('0',' ')
        answer.append(temp)
        print(answer)
        
    return answer

solution(	6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])