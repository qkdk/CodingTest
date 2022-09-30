def solution(n):
    arr = []
    for i in range(1, n + 1):
        tmp = []
        for j in range(1, i + 1):
            tmp.append(0)
        arr.append(tmp)

    # 3가지 경우의 수 왼쪽 아레, 오른쪽, 왼쪽 위 -> 나머지로 구분
    num = 1
    x, y = 0, -1

    for i in range(0, n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1
            arr[y][x] = num
            num += 1

    answer = []
    for i in arr:
        answer.extend(i)

    return answer


solution(4)
