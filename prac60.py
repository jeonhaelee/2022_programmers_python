# 거리두기 확인하기
# 다시 생각해보자!
# 어차피 왼쪽 위에서 오른쪽 아래로 내려가는거니까...
# 기준 p에서 오른쪽이랑 아래랑 오른쪽 아래 대각선만 봐도 되는거 아닌가?
# 오른쪽에 X가 있으면 2오른쪽은 생각 안 해도 되고, 아래쪽에 X가 있으면 2아래쪽은 생각 안 해도 되고,
# 오른쪽에 X, 아래쪽에 X가 있으면 오른쪽아래대각선은 생각 안 해도 되니까.
# 이것들 중 X가 없을 경우에만 한칸 더 가서 P인지 아닌지만 따져주면 될 듯!!!



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