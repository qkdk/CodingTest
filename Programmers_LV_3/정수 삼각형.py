def solution(triangle):
    for floor in range(len(triangle)):
        for value in range(len(triangle[floor])):
            check_floor = floor - 1
            check_left = value - 1
            check_right = value

            if check_floor < 0:
                continue

            # 왼쪽 위 값 존재여부 체크
            if check_left < 0:
                left_value = 0
            else:
                left_value = triangle[check_floor][check_left]

            # 오른쪽 위 값 존재 여부 체크
            try:
                right_value = triangle[check_floor][check_right]
            except:
                right_value = 0

            triangle[floor][value] = max(left_value, right_value) + triangle[floor][value]

    return max(triangle[-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
