class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {']' : '[', 
                        ')' : '(', 
                        '}' : '{'
                        }

        cnt = 0
        while cnt < len(s):
            #만약 여는 괄호면
            if s[cnt] not in bracket_dict:
                stack.append(s[cnt])
            
            #만약 닫는 괄호고 쌍이면 빼 아니면 
            else:
                if stack and stack[-1] == bracket_dict[s[cnt]]:
                    stack.pop()
                else:
                    return False
                
            cnt += 1
            
        if len(stack) == 0:
            return True
        return False
