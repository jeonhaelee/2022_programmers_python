# import numpy as np

# def solution(arr1, arr2):
#     answer = [[]]
#     arr1 = np.array(arr1, dtype=np.int64)
#     arr2 = np.array(arr2, dtype=np.int64)
#     result = arr1.dot(arr2)

#     answer = []
#     for i in range(len(result)):
#         sub_answer = []
#         for j in range(len(result[0])):
#             sub_answer.append(result[i,j])
#         answer.append(sub_answer)
#     return answer


def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sub_answer = []
        for j in range(len(arr2)):
            val = 0
            for k in range(len(arr2[0])):
                val += arr1[i][k] * arr2[k][j]
            sub_answer.append(val)
        answer.append(sub_answer)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

