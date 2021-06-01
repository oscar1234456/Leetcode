class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1<<k
        mySet = set()
        
        
        for i in range(k, len(s)+1):
            now = s[i-k:i]
            if now not in mySet:
                mySet.add(now)
                need -= 1
                if need == 0:
                    return True
        return False