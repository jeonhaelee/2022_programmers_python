# 비밀지도
# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 
# 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append([])

    arr1_fin = []
    for num in arr1:
        str = list(bin(num)[2:])
        while len(str) != n:
            str.insert(0, '0')
        arr1_fin.append(str)
    
    arr2_fin = []
    for num in arr2:
        str = list(bin(num)[2:])
        while len(str) != n:
            str.insert(0, '0')
        arr1_fin.append(str)
    
    # 만약 숫자의 길이가 5가 아닐경우가 있으니,
    # 일단 n * n answer을 만들어주고 0을 채워넣자.

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

