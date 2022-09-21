def solution(words):
    alpha = ['A', 'E', 'I', 'O', 'U']
    tmp = []
    for a in alpha:
        tmp.append(a)
        for b in alpha:
            tmp.append(a + b)
            for c in alpha:
                tmp.append(a + b + c)
                for d in alpha:
                    tmp.append(a + b + c + d)
                    for e in alpha:
                        tmp.append(a + b + c + d + e)

    for i in range(len(tmp)):
        if words == tmp[i]:
            return i + 1


solution("AAAAE")
