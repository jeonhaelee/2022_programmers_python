from pymysql import NULL


def solution(numbers):
    answer = ''
    sub_number = []
    for i in range(len(numbers)):
        if str(numbers[i])[0] == 9:
            sub_number.append(numbers[i])
    return answer

numbers = [3, 30, 34, 5, 9]

thousand = []
hundred = [[],[],[],[],[],[],[],[],[]]
ten = [[],[],[],[],[],[],[],[],[]]
one = [[],[],[],[],[],[],[],[],[]]

for i in numbers:
    if i == 1000 or i == 0:
        thousand.append(i)
    if i // 10 == 0:
        one[int(str(i)[0])-1].append(i)
    elif i // 100 == 0:
        ten[int(str(i)[0])-1].append(i)
    elif i // 1000 == 0:
        hundred[int(str(i)[0])-1].append(i)
        

thousand.sort()

for i in range(9):
    hundred[i-1].sort(reverse=True)
    ten[i-1].sort(reverse=True)
    one[i-1].sort(reverse=True)

answer = ''
for i in range(9,-1,-1):
    for j in one[i-1]:
        answer += str(j)
    for j in ten[i-1]:
        answer += str(j)
    for j in hundred[i-1]:
        answer += str(j)

for i in range(len(thousand)):
    answer += str(i)

print(hundred)
print(ten)
print(one)
print(answer)