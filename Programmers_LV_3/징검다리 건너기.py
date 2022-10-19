# def solution(stones, k):
#     left = 1
#     right = 200000000
#     while left <= right:
#         temp = stones.copy()
#         mid = (left + right) // 2
#         cnt = 0
#         for t in temp:
#             if t - mid <= 0:
#                 cnt += 1
#             else:
#                 cnt = 0
#             if cnt >= k:
#                 break
#         if cnt >= k:
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return left

def solution(stones, k):
    left = 0
    right = 200000000

    count = 0
    while left <= right:
        mid = (right + left) // 2

        for stone in stones:
            if stone - mid > 0:
                count = 0
            else:
                count += 1

            if count >= k:
                right = mid - 1
                break
        else:
            left = mid + 1

    print(left)

    return


# 왜 이분 탐색에서는 left > right 되는 시점에 탐색을 종료하느가
# 이분 탐색을 진행하면 결국 하나의 값만 남는데 거기서 +1 이 되면 left > rihgt 가 성립되기 때문

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
