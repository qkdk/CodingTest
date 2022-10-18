import math


# def solution(n, stations, w):
#     answer = 0
#
#     coverage = [0] * (n + 1)
#     coverage[0] = -1
#     for station in stations:
#         for i in range(station - w, station + w + 1):
#             if i > n:
#                 break
#             coverage[i] = 1
#
#     count = 0
#     for i in range(1, n + 1):
#         if coverage[i] == 1 and count != 0:
#             answer += math.ceil(count / (2 * w + 1))
#             count = 0
#         if coverage[i] == 1:
#             continue
#         count += 1
#
#     answer += math.ceil(count / (2 * w + 1))
#     return answer

def solution(n, stations, w):
    answer = 0
    dist = []
    # 기지국과 기지국 사이의 전파가 도달하지 않는 거리
    for i in range(1, len(stations)):
        dist.append((stations[i] - w - 1) - (stations[i - 1] + w))

    # 기지국에 닫지 않는 맨 앞 부분
    dist.append(stations[0] - w - 1)
    # 기지국에 닫지 않는 맨 뒷 부분
    dist.append(n - (stations[-1] + w))

    for i in dist:
        if i < 0:
            continue
        else:
            answer += math.ceil(i / (2 * w + 1))

    return answer


solution(11, [4, 11], 1)
# solution(16, [9], 2)
