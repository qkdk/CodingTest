count_zero = 0
count_one = 0


def solution(arr):
    answer = []
    global count_zero
    global count_one

    check_matrix(arr)
    answer.append(count_zero)
    answer.append(count_one)
    print(answer)
    return answer


def check_matrix(arr):
    global count_zero
    global count_one

    check_flag = arr[0][0]
    len_flag = int(len(arr) / 2)
    # [[1]]
    if len(arr) == 1:
        if check_flag == 0:
            count_zero += 1
        else:
            count_one += 1
        return

    # [[1,1],[1,2]]
    for i in arr:
        for j in i:
            if j != check_flag:
                # 4등분 후 check_matrix 실행하는 로직
                tmp_arr = []
                for a in range(len_flag):
                    tmp_arr.append(arr[a][:len_flag])
                check_matrix(tmp_arr)

                tmp_arr = []
                for a in range(len_flag):
                    tmp_arr.append(arr[a][len_flag: len(arr)])
                check_matrix(tmp_arr)

                tmp_arr = []
                for a in range(len_flag, len(arr)):
                    tmp_arr.append(arr[a][:len_flag])
                check_matrix(tmp_arr)

                tmp_arr = []
                for a in range(len_flag, len(arr)):
                    tmp_arr.append(arr[a][len_flag: len(arr)])
                check_matrix(tmp_arr)

                return

    if check_flag == 0:
        count_zero += 1
    else:
        count_one += 1

    return


solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
