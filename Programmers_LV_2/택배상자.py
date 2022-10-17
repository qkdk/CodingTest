def solution(order):
    INF = int(1e9)
    flag = 0
    boxes = [INF] * len(order)
    boxes.extend([x for x in range(len(order), 0, -1)])
    stack = [0] * len(order)

    try:
        while True:
            tmp = order[flag]
            if boxes[-1] > tmp and stack[-1] != tmp:
                break

            if tmp == boxes[-1]:
                boxes.pop()
                flag += 1
            elif tmp == stack[-1]:
                stack.pop()
                flag += 1
            else:
                stack.append(boxes.pop())
    except:
        return flag

    return flag


# solution([4, 3, 1, 2, 5])
solution([5, 4, 3, 2, 1])
