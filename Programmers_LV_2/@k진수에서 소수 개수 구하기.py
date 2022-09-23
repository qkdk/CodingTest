import math


def solution(n, k):
    answer = 0
    num = ""
    # 진수 변환
    while n > k:
        r = str(n % k)
        n = n // k
        num = r + num
    num = str(n) + num

    nums = num.split("0")
    for i in nums:
        if check_prime(i):
            answer += 1

    print(answer)
    return answer


def check_prime(number):
    if number == '' or number == '1':
        return False

    number = int(number)

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


# solution(437674, 3)
solution(110011, 10)
