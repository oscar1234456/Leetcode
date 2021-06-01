class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1s = ""
        word2s = ""
        for i in word1:
            word1s += i
        for j in word2:
            word2s += j
        
        return True if (word1s == word2s) else False
# Second Solution (Faster than first)
# class Solution:
#     def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    
#         return ''.join(word1) == ''.join(word2)

#String is immutable object.