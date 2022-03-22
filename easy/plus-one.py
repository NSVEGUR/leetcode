from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            val = digits[i] + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            digits[i] = val
        if carry == 1:
            digits.append(1)
        digits = digits[::-1]
        return digits


sol = Solution()
print(sol.plusOne([9]))
