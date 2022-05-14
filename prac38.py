
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

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]