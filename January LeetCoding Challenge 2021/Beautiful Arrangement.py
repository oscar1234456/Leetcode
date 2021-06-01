class Solution:
    count = 0
    ans = list()
    num = list()
    checked = list()
    def countArrangement(self, n: int) -> int:
        self.num = [i for i in range(n+1)]
        self.checked = [False for _ in range(n+1)]
        self.backTracking(n)
        return self.count
    
    def backTracking(self, n):
        if len(self.ans) == n:
            self.count+=1
            return
        for i in self.num[1:]:
            if ((not self.checked[i]) and ((len(self.ans)+1)%i == 0 or i % (len(self.ans)+1) == 0  )):
                self.ans.append(i)
                self.checked[i] = True
                self.backTracking(n)
                self.ans.remove(i)
                self.checked[i] = False
        
                