
# def is_scov_all_k(scoville, k):
#     for i in scoville:
#         if i < k:
#             return False
#     return True

# def solution(scoville, k):
#     count = 0
#     scoville.sort()
#     while is_scov_all_k(scoville, k) == False:
#         scoville[0] = scoville[0] + (scoville[1] * 2)
#         del scoville[1]
#         count += 1
#         if len(scoville) == 1:
#             if is_scov_all_k(scoville, k) == False:
#                 return -1
#     return count

# scoville = [1, 2, 3, 9, 10, 12]
# k = 7
# print(solution(scoville, k))


import heapq as h

def is_scov_all_k(scoville, k):
    for i in scoville:
        if i < k:
            return False
    return True

def solution(scoville, k):
    count = 0
    while is_scov_all_k(scoville, k) == False:
        num = h.heappop(scoville)
        num += h.heappop(scoville)*2
        h.heappush(scoville,num)
        count += 1
        if len(scoville) == 1:
            if is_scov_all_k(scoville, k) == False:
                return -1
    return count

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))