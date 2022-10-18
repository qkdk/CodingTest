def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    while B:
        num = B.pop()
        for i in range(len(A) - 1, -1, -1):
            if num > A[i]:
                answer += 1
                A.pop(i)
                break

    return answer


solution([5, 1, 3, 7], [2, 2, 6, 8])
