# 수식 최대화
# +, -, *
# 아니지. 우선순위 높은게 뒤쪽에 나올 경우도 생각하면 앞 뒤 숫자를 다 생각해야지.
# 우선순위 젤 높은게 -라면, -위치 찾아서 앞 뒤 숫자 구해주고, 앞 - 뒤 위치에 연산 결과 숫자를 넣어주는 식으로?

from itertools import permutations

def solution(expression):

    numbers = []; cal = []
    num = ""
    for i in range(len(expression)):
        if expression[i].isdigit() :
            num += expression[i]
        else:
            cal.append(expression[i])
            numbers.append(int(num))
            num = ""
    numbers.append(int(num))
    
    print(f'numbers : {numbers}')
    print(f'cal : {cal}')


    cals_permutations = []
    cals_permutations.append(list(permutations(set(cal))))
    
    print(cals_permutations)
    
    # cals 돌면서 cal 우선순위대로 숫자 계산해서 가장 높은 숫자 리턴
    
    # 만약 우선순위 순서가 -, +, *라면
    
    results = []
    
    # 만약 -, +, * 순서라면,
    
    result = 0
    
    while '-' in cal:
        idx = cal.index('-')
        result = numbers[idx]
        result -= numbers[idx+1]
        numbers[idx] = result
        del numbers[idx+1]
        del cal[idx]
        print("==============")
        print(f'result : {result}')
        print(f'numbers : {numbers}')
        print(f'cal : {cal}')
    

    while '+' in cal:
        idx = cal.index('+')
        result = numbers[idx]
        result += numbers[idx+1]
        numbers[idx] = result
        del numbers[idx+1]
        del cal[idx]
        print("==============")
        print(f'result : {result}')
        print(f'numbers : {numbers}')
        print(f'cal : {cal}')
    

    while '*' in cal:
        idx = cal.index('*')
        result = numbers[idx]
        result *= numbers[idx+1]
        numbers[idx] = result
        del numbers[idx+1]
        del cal[idx]
        print("==============")
        print(f'result : {result}')
        print(f'numbers : {numbers}')
        print(f'cal : {cal}')
        
    results.append(abs(result))
    
    print(results)
    answer = max(results)
    
    return answer

expression = "100-200*300-500+20"
print(solution(expression)) #60420