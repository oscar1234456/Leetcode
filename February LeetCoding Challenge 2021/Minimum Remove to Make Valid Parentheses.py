#solution1: not complete (12/60cases)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        finalRes = ""
        open = 0
        i=0
        c = 0
        for item in s:
            if item == "(":
                open += 1
                res+=item
            elif item == ")":
                if open > 0:
                    res+=item
                    open -= 1
                if open == 0:
                    i = c+1
            else:
                # letters
                res += item
            c+=1
        print(res)
        print(i)
        length = len(res)
        #if open > 0  => delete from leftest "("  for open times
        
        while open>0 and i<length:
            if res[i]=="(":
                open-=1
            else:
                finalRes+=res[i]
            i+=1
        
        if i<length:
            finalRes += res[i:]
        
        return finalRes

#solution2 (success) (stack)

# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         s = list(s)
#         stack = list()
        
#         for i, char in enumerate(s):
#             if char == "(":
#                 stack.append(i)
#             elif char == ")":
#                 if stack:
#                     stack.pop()
#                 else:
#                     s[i] = ""
#         while stack:
#             s[stack.pop()] = ""
        
#         return "".join(s)