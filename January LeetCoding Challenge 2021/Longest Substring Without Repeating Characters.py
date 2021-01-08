class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longestPath = 1
        nowPath = 1
        tempSet = set()
        for i in range(len(s)):
            now = s[i]
            tempSet = set(now)
            for j in range(i+1, len(s)):
                if s[j] not in tempSet:
                    nowPath += 1
                    tempSet.add(s[j])
                else:
                    break
            if nowPath > longestPath:
                longestPath = nowPath
            nowPath = 1
        return longestPath