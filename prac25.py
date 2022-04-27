from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_count(sub_nums, i):
    count = 0
    sub_stack = []
    for n in sub_nums:
        if int(n[0]) == 0:
            continue
        word = ''.join(n)
        number = int(word)
        if number in sub_stack:
            continue
        else: 
            sub_stack.append(number)
            if is_prime(number):
                count += 1
    return count
    
def solution(numbers):
    answer = 0
    
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i])
    
    stack = []
    for i in range(len(nums)):
        if nums[i] in stack:
            continue
        else:
            if is_prime(int(nums[i])):
                stack.append(nums[i])
                answer += 1
    
    for i in range(2, len(nums)+1):
        sub_nums = list(permutations(nums, i))
        answer += prime_count(sub_nums, i)
        
    return answer
