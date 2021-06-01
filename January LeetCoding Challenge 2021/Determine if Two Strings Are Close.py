from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        keep1 = defaultdict(int)
        keep2 = defaultdict(int)
        
        for i in range(len(word1)):
            keep1[word1[i]] += 1
            keep2[word2[i]] += 1
            
        # word1Set = set(keep1.keys())
        # word2Set = set(keep2.keys())
        
        if keep1.keys() != keep2.keys():
            return False
        
        word1NumSet = set(keep1.values())
        word2NumSet = set(keep2.values())
        
        if word1NumSet != word2NumSet:
            return False
        
        return True
            
        
#292ms 29.68%