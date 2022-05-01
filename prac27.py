

def solution(arr1, arr2):
    h = len(arr1)
    w = len(arr2[0])
    answer = []
    for i in range(h):
        sub_answer = []
        for j in range(w):
            sub_answer.append(0)
        answer.append(sub_answer)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

