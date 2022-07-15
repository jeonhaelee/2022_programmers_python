# 거리두기 확인하기

# def solution(places):
#     answer = []
#     return answer

# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
#           ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#           ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# print(solution(places)) # [1, 0, 1, 1, 1]


place = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]

place_list = []

for i in range(len(place)):
    place_list.append((list(place[i])))
    
print(place_list)