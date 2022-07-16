# 거리두기 확인하기
# 다시 생각해보자!
# 어차피 왼쪽 위에서 오른쪽 아래로 내려가는거니까...
# 기준 p에서 오른쪽이랑 아래랑 오른쪽 아래 대각선만 봐도 되는거 아닌가?
# 오른쪽에 X가 있으면 2오른쪽은 생각 안 해도 되고, 아래쪽에 X가 있으면 2아래쪽은 생각 안 해도 되고,
# 오른쪽에 X, 아래쪽에 X가 있으면 오른쪽아래대각선은 생각 안 해도 되니까.
# 이것들 중 X가 없을 경우에만 한칸 더 가서 P인지 아닌지만 따져주면 될 듯!!!

place = ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]

def check_place(place):
    place_list = []

    for i in range(len(place)):
        place_list.append((list(place[i])))
        
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check_place(place))
        
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places)) # [1, 0, 1, 1, 1]


