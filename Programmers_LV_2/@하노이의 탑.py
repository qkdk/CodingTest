def solution(n):
    answer = []

    def hanoi(num, start, destination, via):
        if num == 1:
            answer.append([start, destination])
            return

        hanoi(num - 1, start, via, destination)

        answer.append([start, destination])

        hanoi(num - 1, via, destination, start)

    hanoi(n, 1, 3, 2)

    return answer


solution(2)
