def solution(routes):
    routes.sort(key=lambda x: x[1])

    camera = -30001
    count = 0
    for route in routes:
        enter = route[0]
        out = route[1]
        if camera < enter:
            # 새로운 카메라가 필요
            camera = out
            count += 1

    return count


solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]])
