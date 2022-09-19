from collections import deque
import math


def solution(fees, records):
    # 번호판 별로 입, 출력시간을 기록한 딕셔너리 생성
    answer = []
    times = {}
    perFees = {}
    for i in records:
        if int(i[6:10]) not in times:
            times[int(i[6:10])] = deque([])
        times[int(i[6:10])].append(int(i[0:2]) * 60 + int(i[3:5]))

    for i in times:
        perFees[i] = 0
        if len(times[i]) % 2 == 1:
            times[i].append(1439)

        while times[i]:
            perFees[i] += times[i][1] - times[i][0]
            times[i].popleft()
            times[i].popleft()

    for i in perFees:
        if perFees[i] < fees[0]:
            perFees[i] = fees[1]
        else:
            perFees[i] = math.ceil((perFees[i] - fees[0]) / fees[2]) * fees[3] + fees[1]

    tmp = sorted(list(perFees.keys()))

    for i in tmp:
        answer.append(perFees[i])
    return answer


solution([180, 5000, 10, 600],
         ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
