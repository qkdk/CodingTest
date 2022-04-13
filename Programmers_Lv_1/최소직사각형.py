def solution(sizes):
    max_x = 0
    max_y = 0

    for i in sizes:
        if i[0] < i[1]:
            temp = i[0]
            i[0] = i[1]
            i[1] = temp
        
        if max_x < i[0]:
            max_x = i[0]
        
        if max_y < i[1]:
            max_y = i[1]

    answer = max_x * max_y

    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])