class KnapsackSolver:
    def __init__(self, W:int, item:list):
        self.W = W
        self.item = item
        self.kmap = [[-1 for j in range(W+1)] for i in range(len(item)+1)]

    def runStart(self):
        for itemId in range(len(self.item)+1):
            for w in range(self.W+1):
                if w == 0 or itemId == 0:
                    self.kmap[itemId][w] = 0
                elif self.item[itemId-1][0] <= w:
                    self.kmap[itemId][w] = max(self.kmap[itemId-1][w], self.kmap[itemId-1][w-(self.item[itemId-1][0])]+self.item[itemId-1][1])
                else:
                    self.kmap[itemId][w] = self.kmap[itemId-1][w]
    
    def showAnswer(self):
        return self.kmap[len(self.item)][self.W]
        



W = 12 #Upper Bound of Bag size
item = [(3,20), (4,45), (9,70), (12,85)] #item (weight,value)
knapsackSolver = KnapsackSolver(W, item)
knapsackSolver.runStart()
print(knapsackSolver.showAnswer())



