class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        store = ''
        for l in s:
            store += l
            if l in result:
                store = store[store.find(l)+1:len(store)]
                if len(store) >= len(result):
                    result = store
            elif len(result) < len(store):
                result = store
        return result


sol = Solution()
print(sol.lengthOfLongestSubstring("jbpnbwwd"))
