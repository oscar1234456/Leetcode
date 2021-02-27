class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = list()
        nowPop = 0
        popLength = len(popped)
        
        for pushItem in pushed:
            stack.append(pushItem)
            
            if popped[nowPop] == pushItem:
                stack.pop()
                nowPop += 1
                while nowPop<popLength and len(stack)>0 and popped[nowPop]==stack[len(stack)-1]:
                    stack.pop()
                    nowPop += 1
        
        for i in range(len(stack)):
            now = stack.pop()
            if now != popped[nowPop]:
                    return False
            nowPop += 1
        return True