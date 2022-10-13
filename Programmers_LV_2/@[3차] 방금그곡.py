def solution(m, musicinfos):
    music = []

    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace("G#", 'g').replace('A#', 'a')

    for musicinfo in musicinfos:
        music.append(musicinfo.split(','))

    for index, i in enumerate(music):
        i[3] = i[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace("G#", 'g').replace('A#', 'a')
        length = len(i[3])
        start_time = i[0].split(':')
        end_time = i[1].split(':')

        time_diff = (int(end_time[0]) - int(start_time[0])) * 60 + int(end_time[1]) - int(start_time[1])

        tmp = ''
        for j in range(time_diff + 1):
            tmp += i[3][j % length]

        i[3] = tmp

    music.sort(key=lambda x: -len(x[3]))

    for i in music:
        if m in i[3]:
            return i[2]

    return "(None)"


# solution("ABCDEFG", ["13:00,13:05,WORLD,ABCDEF", "12:00,12:14,HELLO,CDEFGAB"])

solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])

# solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
