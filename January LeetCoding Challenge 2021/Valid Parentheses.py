class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        myStack = list()
        for i in s:
            if i == "(":
                myStack.append("(")
            elif i == "{":
                myStack.append("{")
            elif i == "[":
                myStack.append("[")
            elif i == ")":
                if len(myStack)>0:
                    temp = myStack.pop()
                else: return False
                if temp != "(":
                    return False
            elif i == "}":
                if len(myStack)>0:
                    temp = myStack.pop()
                else: return False
                if temp != "{":
                    return False
            else:
                # i == "]"
                if len(myStack)>0:
                    temp = myStack.pop()
                else: return False
                if temp != "[":
                    return False
        return True if len(myStack)==0 else False

#Solution 2: 8ms Pretty Code (Other people)
# class Solution:
    # def isValid(self, s: str) -> bool:
    #     ob = []
    #     brackets = {'(':')', '{':'}', '[':']'}
    #     for bracket in s:
    #         if bracket in brackets:
    #             ob.append(bracket)
    #             continue
    #         if not ob:
    #             return False
    #         b = ob.pop()
    #         if bracket != brackets[b]:
    #             return False
    #     return not ob
            