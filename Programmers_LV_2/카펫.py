import math


def check_brown(brown, x, y):
    return 2 * x + 2 * y + 4 == brown


def solution(brown, yellow):
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            y = i
            x = yellow // i
            if check_brown(brown, x, y):
                return [x + 2, y + 2]


solution(10, 2)
