# 비밀지도
# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 
# 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append([])

    arr1_fin = []
    for num in arr1:
        str = bin(num)
        arr1_fin.append(list(str[2:]))
    
    arr2_fin = []
    for num in arr2:
        str = bin(num)
        arr2_fin.append(list(str[2:]))
    

    for i in range(n):
        for j in range(n):
            if arr1_fin[i][j] == '0' and arr2_fin[i][j] == '0':
                answer[i][j] = " "
            else:
                answer[i][j] = "#"
                
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2)) # ["#####","# # #", "### #", "# ##", "#####"]

# n = 6
# arr1 = [46, 33, 33 ,22, 31, 50]
# arr2 = [27 ,56, 19, 14, 14, 10]
# print(solution(n, arr1, arr2)) # ["######", "### #", "## ##", " #### ", " #####", "### # "]
