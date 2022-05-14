
# def weight_is_possible(bridge, weight):
#     sum = 0
#     for w in bridge:
#         sum += w
#     if sum <= weight:
#         return True
#     else: return False

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [-1]*bridge_length
    
#     bridge[-1] = truck_weights[0]
#     del truck_weights[0]
#     answer += 1
#     print("answer : {}".format(answer))
    
#     while len(truck_weights) > 0:
#         bridge[0], bridge[1] = bridge[1], -1
#         bridge[-1] = truck_weights[0]
#         if weight_is_possible(bridge, weight) :
#             del truck_weights[0]
#             print("answer : {}".format(answer))
#             print("bridge : {}".format(bridge))
#             print("truck_weights : {}".format(truck_weights))
#             answer += 1
#         else:
#             bridge[-1] = -1
#             print("answer : {}".format(answer))
#             print("bridge : {}".format(bridge))
#             print("truck_weights : {}".format(truck_weights))
#             answer += 1
            
#     answer += bridge_length
#     return answer



def weight_is_possible(bridge, weight, truck_weights):
    sum = 0
    for i in range(1, len(bridge)):
        if bridge[i] != -1:
            sum += bridge[i]
    if sum + truck_weights[0] <= weight:
        return True
    else: return False

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [-1]*bridge_length
    
    del bridge[0]
    bridge.append(truck_weights[0])
    del truck_weights[0]
    answer += 1
    print("answer : {}".format(answer))
    print("bridge : {}".format(bridge))
    print("truck_weights : {}".format(truck_weights))
    
    while len(truck_weights) > 0:
        if weight_is_possible(bridge, weight, truck_weights) :
            del bridge[0]
            bridge.append(truck_weights[0])
            del truck_weights[0]
            print("answer : {}".format(answer))
            print("bridge : {}".format(bridge))
            print("truck_weights : {}".format(truck_weights))
            answer += 1
        else:
            del bridge[0]
            bridge.append(-1)
            print("answer : {}".format(answer))
            print("bridge : {}".format(bridge))
            print("truck_weights : {}".format(truck_weights))
            answer += 1
            
    answer += bridge_length
    return answer


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))