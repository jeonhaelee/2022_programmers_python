
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
    
    bridge[-1] = truck_weights[0]
    del truck_weights[0]
    answer += 1
    
    while len(truck_weights) > 0:
        bridge[0], bridge[1] = bridge[1], -1
        bridge[-1] = truck_weights[0]
        if weight_is_possible(bridge, weight) :
            del truck_weights[0]
            print("bridge : {}".format(bridge))
            print("truck_weights : {}".format(truck_weights))
            answer += 1
        else:
            bridge[-1] = -1
            print("bridge : {}".format(bridge))
            print("truck_weights : {}".format(truck_weights))
            answer += 1

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))