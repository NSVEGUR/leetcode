from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        flag = False
        if len(strs) == 0:
            return ''
        for ltr in strs[0]:
            if flag:
                break
            pref += ltr
            for i in range(1, len(strs)):
                if not strs[i].startswith(pref):
                    pref = pref[0:len(pref)-1]
                    flag = True
                    break
        return pref
