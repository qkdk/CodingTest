def solution(n):
    count = str(bin(n)).count("1")

    while True:
        n += 1
        if str(bin(n)).count("1") == count:
            return n


solution(78)
