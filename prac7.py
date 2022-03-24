def solution(sizes):
    answer = 0
    max_w = sizes[0][0]
    max_h = sizes[0][1]
    for i in range(len(sizes)):
        if sizes[i][0] <= max_w and sizes[i][1] <= max_h:
            continue
        elif sizes[i][0] <= max_h and sizes[i][1] <= max_w:
            continue
        elif sizes[i][0] >= max_w and sizes[i][1] >= max_h:
            max_w = sizes[i][0]
            max_h = sizes[i][1]  
        elif sizes[i][0] >= max_h and sizes[i][1] >= max_w:
            max_w = sizes[i][1]
            max_h = sizes[i][0]
        elif sizes[i][0] >= max_w and sizes[i][1] <= max_h:
            if sizes[i][1] <= max_w:
                if sizes[i][0] * max_h <= max_w * sizes[i][0]:
                    max_w = sizes[i][0]
                else : max_h = sizes[i][0]
            else : 
                if max_h >= sizes[i][1]:
                    max_w = sizes[i][0]
                else : max_w = sizes[i][0]; max_h = sizes[i][1]
        elif sizes[i][0] <= max_w and sizes[i][1] >= max_h:
            if sizes[i][0] <= max_h:
                if max_w * sizes[i][1] <= sizes[i][1] * max_h:
                    max_h = sizes[i][1]
                else : max_w = sizes[i][1]
            else : 
                if max_w >= sizes[i][0]:
                    max_h = sizes[i][1]
                else : max_w = sizes[i][0]; max_h = sizes[i][1]

    answer = max_h * max_w
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))