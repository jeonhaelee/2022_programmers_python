import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    arr1 = np.array(arr1, dtype=np.int64)
    arr2 = np.array(arr2, dtype=np.int64)
    result = arr1.dot(arr2)
    
    answer = []
    for i in range(len(result)):
        sub_answer = []
        for j in range(len(result[0])):
            sub_answer.append(result[i,j])
        answer.append(sub_answer)
    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))

