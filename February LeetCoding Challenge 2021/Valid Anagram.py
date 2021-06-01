from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def beZero():
            return 0
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        
        for item in s:
            dict1[item]+=1
        
        for item in t:
            dict2[item]+=1
            
        for i in dict1:
            if i not in dict2:
                return False
            elif dict1[i]!=dict2[i]:
                return False
            
        return True
            