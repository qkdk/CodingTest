def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp_list = []
        for k in range(len(arr2[0])):
            tmp = 0
            for j in range(len(arr1[i])):
                tmp += arr1[i][j] * arr2[j][k]
            tmp_list.append(tmp)
        answer.append(tmp_list)
    return answer


# solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
solution([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]])

# 2 3 2   5 4 3
# 4 2 4   2 4 1
# 3 1 4   4 1 1
