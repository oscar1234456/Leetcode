# Solution1 (not successful)
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.countDict = defaultdict(int)
        self.group = defaultdict(list)
        self.stack = list()
        # self.maxCount = 0

    def push(self, x: int) -> None:
        if x in self.group[self.countDict[x]]:
            self.group[self.countDict[x]].remove(x)
        self.countDict[x]+=1
        self.group[self.countDict[x]].append(x)
        self.stack.append(x)

    def pop(self) -> int:
        temp = set()
        maxCount = 0
        for value in self.countDict.values():
            if value>maxCount:
                maxCount = value
        res = self.group[maxCount][0]
        self.countDict[res]-=1
        self.group[maxCount].remove(res)
        self.group[self.countDict[res]].append(res)
        
        
        return res
            
        # for i in range(len(stack)-1,-1,-1):
        #     if self.stack[i] in temp:
        #         res =  self.stack[i]
        #         self.stack = self.stack[0:i]+self.stack[i+1:]
        #         return res
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


#Solution2
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x