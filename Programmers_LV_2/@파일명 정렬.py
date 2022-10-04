def solution(files):
    answer = []
    index = 0
    for file in files:
        head = ''
        number = '0'
        check = False
        for i in file:
            if i.isdigit() and len(number):
                number += str(i)
                check = True
            elif not check:
                head += i.upper()
            else:
                break
        answer.append([head, int(number), index, file])
        index += 1

    answer.sort()
    return [answer[i][3] for i in range(len(files))]
