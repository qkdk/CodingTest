def solution(places):

    answer = []
    coord = []
    block = []
    flag = 0

    for i in range(len(places)):
        for y in range(len(places[i])):
            for x in range(len(places[i][y])):
                if places[i][y][x] == "P":
                    coord.append([i,x,y])
                elif places[i][y][x] == "X":
                    block.append([i,x,y])

    while flag < len(coord) - 1:
        for k in range(flag + 1, len(coord)):
            manhattan = abs(coord[flag][1] - coord[k][1]) + abs(coord[flag][2] - coord[k][2])
            if manhattan < 3:
                alist = [[coord[0][0],a,b] for a in range(min(coord[flag][1], coord[k][1]),max(coord[flag][1], coord[k][1]) +1) for b in range(min(coord[flag][2], coord[k][2]),max(coord[flag][2], coord[k][2])+1)]
                for c in alist:
                    if c in block:
                        pass

        flag += 1



    print(coord)
    print(block)
    print(answer)

    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]])


