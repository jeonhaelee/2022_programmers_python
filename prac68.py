# 수식 최대화
# +, -, *
# 아니지. 우선순위 높은게 뒤쪽에 나올 경우도 생각하면 앞 뒤 숫자를 다 생각해야지.


from itertools import permutations

def solution(expression):

    numbers = []; cal = []
    num = ""
    for i in range(len(expression)):
        if expression[i].isdigit() :
            num += expression[i]
        else:
            cal.append(expression[i])
            numbers.append(num)
            num = ""
    
    num_cal = []
    num_cal.append(numbers[0])
    
    for i in range(1, len(numbers)):
        num_cal.append(cal[i] + numbers[i])
    
    cals_permutations = []
    cals_permutations.append(list(permutations(set(cal))))
    
    print(cals_permutations)
    
    # cals 돌면서 cal 우선순위대로 숫자 계산해서 가장 높은 숫자 리턴
    
    # 만약 우선순위 순서가 -, +, *라면
    
    results = []
    result = int(num_cal[0])
    for i in range(1, len(num_cal)):
        if num_cal[i][0] == '-':
            result -= int(num_cal[i][1:])
    
    for i in range(1, len(num_cal)):
        if num_cal[i][0] == '+':
            result += int(num_cal[i][1:])
            
    for i in range(1, len(num_cal)):
        if num_cal[i][0] == '*':
            result *= int(num_cal[i][1:])
            
    results.append(abs(result))
    
    answer = max(results)
    
    return answer

expression = "100-200*300-500+20"
print(solution(expression)) #60420