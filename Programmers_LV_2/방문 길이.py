def solution(dirs):
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    current_loc = (0, 0)
    loc_memory = []

    for dir in dirs:
        dx = move[dir][0]
        dy = move[dir][1]

        nx = dx + current_loc[0]
        ny = dy + current_loc[1]

        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue

        loc_memory.append((current_loc, (nx, ny)))
        current_loc = (nx, ny)

    answer = len(loc_memory)

    for i in range(len(loc_memory)):
        reverse_i = (loc_memory[i][1], loc_memory[i][0])
        for j in range(i + 1, len(loc_memory)):
            if loc_memory[i] == loc_memory[j] or reverse_i == loc_memory[j]:
                answer -= 1
                break

    return answer


solution("ULURRDLLU")
