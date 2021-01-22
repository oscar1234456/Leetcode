class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        myStack = list()
        allow = len(nums)-k
        for i in nums:
            while myStack and allow and i < myStack[-1] :
                myStack.pop()
                allow -= 1
            myStack.append(i)
        return myStack[:k]
        