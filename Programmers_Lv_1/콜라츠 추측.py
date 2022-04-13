def solution(num):
    flag = num%2

    for i in range(500):
        if num == 1:
            return i
        elif flag == 0:
            num = num /2
            flag = num%2
        else:
            num = num* 3 + 1
            flag = num%2

    return -1

solution(6)