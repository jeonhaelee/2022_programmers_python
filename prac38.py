
def weight_is_possible(bridge, weight):
    sum = 0
    for w in bridge:
        sum += w
    if sum <= weight:
        return True
    else: return False

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [-1]*bridge_length
    
    while len(truck_weights) > 0:
        if bridge[0] == -1:
            bridge[0] = truck_weights[0]
            answer += 1
            continue
        bridge[0], bridge[1] = bridge[1], -1
        if bridge[-1] == -1:
            bridge[-1] = truck_weights[0]
            if weight_is_possible(bridge, weight) :
                del truck_weights[0]
                continue
            else:
                bridge[-1] = -1
        answer += 1
            
    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]