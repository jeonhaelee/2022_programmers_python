from itertools import permutations

class Stack :
    def __init__(self) -> None:
        self.stack = []
    
    def is_prime(self,n):
        if n == 0 or n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def prime_count(self,sub_nums, i):
        count = 0
        for n in sub_nums:
            word = ""
            for i in range(len(n)):
                word += n[i]
            number = int(word)
            if self.is_prime(number):
                count += 1
        return count
        
    def solution(self, numbers):
        answer = 0
        
        nums = []
        for i in range(len(numbers)):
            nums.append(numbers[i])
        print("nums : {}".format(nums))
        
        for i in range(len(nums)):
            if i in self.stack:
                continue
            else:
                if self.is_prime(int(i)):
                    self.stack.append(i)
                    answer += 1
                
        for i in range(2, len(nums)+1):
            sub_nums = list(permutations(nums, i))
            print("{}개씩 sub_nums : {}".format(i, sub_nums))
            answer += self.prime_count(sub_nums, i)
            
        return answer

numbers = "011"
print(Stack.solution(numbers))