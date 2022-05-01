

def solution(arr1, arr2):
    h = len(arr1) # arr1 행 길이
    w = len(arr2[0]) # arr2 열 길이
    answer = []
    for i in range(h):
        sub_answer = []
        for j in range(w):
            sub_answer.append(0)
        answer.append(sub_answer)
        
    for i in range(h):
        for j in range(w):
            for k in range(h):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

