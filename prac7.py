def solution(sizes):
    answer = 0
    max_w = sizes[0][0]
    max_h = sizes[0][1]
    for i in range(len(sizes)):
        if sizes[i][0] >= max_w:
            if sizes[i][0] <= max_h and sizes[i][1] <= max_w:
                continue
            if sizes[i][0]-max_w >= sizes[i][0]-max_h:
                max_h = sizes[i][0]
            else : max_w = sizes[i][0]
        if sizes[i][1] >= max_h:
            if sizes[i][0] <= max_h and sizes[i][1] <= max_w:
                continue
            if sizes[i][1]-max_h >= sizes[i][1]-max_w:
                max_w = sizes[i][1]
                if sizes[i][0] >= max_h:
                    max_h = sizes[i][0]
            else : max_h = sizes[i][1]
    answer = max_h * max_w
    return answer

sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(sizes))