def solution(numbers):

    answer = -1
    checkNumber = [x for x in range(10)]

    for i in range(len(checkNumber)):
        if i in numbers:
            checkNumber.remove(i)

    answer = sum(checkNumber)
    return answer

numbers = [1, 2, 3, 4, 6, 7, 8, 0]
solution(numbers)

# for i in checkNumber 에서 for 문안에서 list 내용이 삭제될경우 for문 전체에 영향을 끼칠 수 있다.