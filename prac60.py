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


    
def check_place(place):
    for i in range(5):
        for j in range(5):
            
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i-1][j]:
                    return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i][j-1]:
                    return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i+1][j]:
                    return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i][j+1]:
                    return 0
            
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i][j-2]:
                    if 'X' != place[i][j-1]:
                        return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i][j+2]:
                    if 'X' != place[i][j+1]:
                        return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i-2][j]:
                    if 'X' != place[i-1][j]:
                        return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i+2][j]:
                    if 'X' != place[i+1][j]:
                        return 0
            
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i-1][j-1]:
                    if 'X' != place[i][j-1] or 'X' != place[i-1][j]:
                        return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i-1][j+1]:
                    if 'X' != place[i][j+1] or 'X' != place[i-1][j]:
                        return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i+1][j-1]:
                    if 'X' != place[i][j-1] or 'X' != place[i+1][j]:
                        return 0
            if i<0 or i>4 or j<0 or j>4:
                pass
            else:
                if 'P' == place[i+1][j+1]:
                    if 'X' != place[i][j+1] or 'X' != place[i][j+1]:
                        return 0
            
    return 1

print(check_place(place))