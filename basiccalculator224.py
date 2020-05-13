class Solution:
    def calculate(self, s: str) -> int:
        #use stack to handle recursive operation.
        pointer = 0
        ans_sofar = 0
        #operand = 1 means "+"
        last_operand = 1
        stack = []
        while pointer < len(s):
            if s[pointer].isnumeric():
                current = ""
                while pointer<len(s) and s[pointer].isnumeric():
                    current += s[pointer]
                    pointer += 1
                
                current_num = int(current)
                
                if last_operand == -1:
                    current_num = -current_num
                ans_sofar += current_num
            elif s[pointer] in "+-":
                if s[pointer] == "+":
                    last_operand = 1
                else:
                    last_operand = -1
                pointer += 1
            elif s[pointer] == "(":
                stack.append(ans_sofar)
                stack.append(last_operand)
                ans_sofar = 0
                last_operand = 1
                pointer += 1
            elif s[pointer] == ")":
                
                operand = stack.pop()
                operator = stack.pop()
                if operand == -1:
                    ans_sofar = -ans_sofar
                operator += ans_sofar
                ans_sofar = operator
                pointer += 1
            else:
                pointer += 1
        if stack:
            while stack:
                current = stack.pop()
                if stack:
                    operand = stack.pop()
                    operator = stack.pop()
                    if operand == -1:
                        current = -current
                    operator += current
                    stack.append(operator)

                else:
                    return current
        else:
            return ans_sofar