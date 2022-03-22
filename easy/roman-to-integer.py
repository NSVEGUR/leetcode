class Solution:

    def findInt(self, s: str) -> int:
        val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        return val[s]

    def romanToInt(self, s: str) -> int:
        result = 0
        present = None
        prev = None
        for i in range(len(s) - 1, -1, -1):
            present = self.findInt(s[i])
            if not prev:
                result += present
                prev = present
            elif prev > present:
                result -= present
                prev = present
            else:
                result += present
                prev = present
        return result
