from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {}
        map['('] = 1
        map['{'] = 2
        map['['] = 3
        map[')'] = 4
        map['}'] = 5
        map[']'] = 6
        s = s[::-1]
        for l in s:
            if l == '}' or l == ']' or l == ')':
                stack.append(map[l])
            else:
                if len(stack) == 0:
                    return False
                elif abs(map[l] - stack[len(stack) - 1]) != 3:
                    return False
                else:
                    stack.pop()
        if stack == []:
            return True
        return False


sol = Solution()
print(sol.isValid("(){}[()[{}]]"))
