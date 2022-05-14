
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [-1]*bridge_length
    weight_sum = 0
    
    del bridge[0]
    bridge.append(truck_weights[0])
    weight_sum += truck_weights[0]
    del truck_weights[0]
    answer += 1
    
    while len(truck_weights) > 0:
        
        if bridge[0] != -1:
            test = weight_sum + truck_weights[0] - bridge[0]
        else: test = weight_sum + truck_weights[0]
        
        if test <= weight :
            if bridge[0] != -1:
                weight_sum -= bridge[0]
            del bridge[0]
            bridge.append(truck_weights[0])
            weight_sum += truck_weights[0]
            del truck_weights[0]
            answer += 1
            
        else:
            if bridge[0] != -1:
                weight_sum -= bridge[0]
            del bridge[0]
            bridge.append(-1)
            answer += 1
            
    answer += bridge_length
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))