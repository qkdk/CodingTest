from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    num_truck = len(truck_weights)
    truck_weights = deque(truck_weights)
    truck_weights.extend([0] * bridge_length)
    bridge_q = deque([0] * bridge_length)
    arrived_q = deque()
    current_weight = 0

    while len(arrived_q) != num_truck:
        time += 1

        if bridge_q[-1] != 0:
            arrived_q.append(bridge_q[-1])
            current_weight -= bridge_q[-1]

        bridge_q.pop()

        # 다리에 있는 차의 무게를 측정
        if current_weight + truck_weights[0] <= weight:
            bridge_q.appendleft(truck_weights.popleft())
            current_weight += bridge_q[0]
        else:
            bridge_q.appendleft(0)

    return time


solution(2, 10, [7, 4, 5, 6])
# solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
