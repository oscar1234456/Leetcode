class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = list()
        
        if S.isdigit():
            res.append(S)
            return res

        for i in range(len(S)):
            if S[i].isalpha():
                temp = list()
                if i<len(S)-1:
                    temp = self.letterCasePermutation(S[i+1:])
                if len(temp)==0:
                    temp = [""]
                for item in temp:
                    res.append(S[:i]+S[i].upper()+item)
                    res.append(S[:i]+S[i].lower()+item)
                break
        return res