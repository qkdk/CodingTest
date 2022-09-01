import math


def basic_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False

    return True


# 약수는 중간까지만 계산하면 된다는점을 이용
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True