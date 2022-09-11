# 문자열 정렬은 아스키로 치환하여 정렬함
def solution(numbers):
    a = list(map(str, numbers))
    a = sorted(a, key=lambda x: x * 3, reverse=True)
    return str(int(''.join(a)))


solution([3, 30, 34, 5, 9])
