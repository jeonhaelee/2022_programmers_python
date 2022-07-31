# 수식 최대화
# +, -, *


from itertools import permutations

def do_minus(numbers_2, cal_2):
    while '-' in cal_2:
        idx = cal_2.index('-')
        result = numbers_2[idx]
        result -= numbers_2[idx+1]
        numbers_2[idx] = result
        del numbers_2[idx+1]
        del cal_2[idx]
        print("==============")
        print(f'result : {result}')
        print(f'numbers : {numbers_2}')
        print(f'cal : {cal_2}')
    return result

def do_plus(numbers_2, cal_2):
    while '+' in cal_2:
        idx = cal_2.index('+')
        result = numbers_2[idx]
        result += numbers_2[idx+1]
        numbers_2[idx] = result
        del numbers_2[idx+1]
        del cal_2[idx]
        print("==============")
        print(f'result : {result}')
        print(f'numbers : {numbers_2}')
        print(f'cal : {cal_2}')
    return result
        
def do_multi(numbers_2, cal_2):
    while '*' in cal_2:
        idx = cal_2.index('*')
        result = numbers_2[idx]
        result *= numbers_2[idx+1]
        numbers_2[idx] = result
        del numbers_2[idx+1]
        del cal_2[idx]
        print("==============")
        print(f'result : {result}')
        print(f'numbers : {numbers_2}')
        print(f'cal : {cal_2}')
    return result




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
    
    results = []
    

    for cals in cals_permutations[0]:
        print(f'cals:{cals}')
        a, b, c = cals[0], cals[1], cals[2]
        
        numbers_2 = numbers
        cal_2 = cal
        
        result = 0
        if a == '-':
            result = do_minus(numbers_2, cal_2)
        elif a == '+':
            result = do_plus(numbers_2, cal_2)
        elif a == '*':
            result = do_multi(numbers_2, cal_2)
            
        if b == '-':
            result = do_minus(numbers_2, cal_2)
        elif b == '+':
            result = do_plus(numbers_2, cal_2)
        elif b == '*':
            result = do_multi(numbers_2, cal_2)
            
        if c == '-':
            result = do_minus(numbers_2, cal_2)
        elif c == '+':
            result = do_plus(numbers_2, cal_2)
        elif c == '*':
            result = do_multi(numbers_2, cal_2)    
        
        results.append(abs(result))
    
    print(results)
    answer = max(results)
    
    return answer

expression = "100-200*300-500+20"
print(solution(expression)) #60420