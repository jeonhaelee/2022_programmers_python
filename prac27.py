

def solution(arr1, arr2):
    h = len(arr1)
    w = len(arr2[0])
    answer = []
    for i in range(h):
        sub_answer = []
        for j in range(w):
            sub_answer.append(0)
        answer.append(sub_answer)
        
    for i in range(h):
        for j in range(len(arr2)):
            for k in range(w):
                answer[i][j] = arr1[i][k] * arr2[k][j]
    
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

