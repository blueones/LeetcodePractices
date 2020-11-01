print("Hello World!")
# stack permutation of a list
# list 1 2 3
# 

# destination : 
# generate all stack permutations of a given listc
class StackPermutation:
    def permutation(self, input_list):
        #return a list of list of all the permutations
        #store permutations in ans
        ans = []
        current_stack = deque()
        def helper(pointer_index, current_permu):
            if len(current_permu) == len(input_list):
                #check if stack is empty
                # when not empty, pop one. 
                # if current_stack:
                #     popped = current_stack.pop()
                #     current_permu.append(popped)
                #     helper(pointer_index, current_permu)
                #     current_permu.pop()
                #     current_stack.append(popped)
                # else:
                ans.append(current_permu.copy())
            else:
                #either push into stack
                if pointer_index < len(input_list):
                    current_stack.append(input_list[pointer_index])
                    helper(pointer_index + 1, current_permu)
                    current_stack.pop()
                # or popping out of stack
                if current_stack:
                    popped = current_stack.pop()
                    current_permu.append(popped)
                    helper(pointer_index, current_permu)
                    current_permu.pop()
                    current_stack.append(popped)
        helper(0, [])
        return ans

print(StackPermutation().permutation([1,2,3,4])) 
# [[3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]
            #第1个数在从0到N-1的位置上。
            # dp[n] = dp[n - 1] * dp[0] + dp[n - 2] * dp[1] + ... + dp[0] * dp[n - 1]
# 卡特兰数