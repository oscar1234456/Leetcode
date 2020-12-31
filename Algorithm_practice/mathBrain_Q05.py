class coinExchanger:
    def __init__(self, amount:int, coin:list):
        self.amount = amount
        self.coin = coin
        self.kmap = [[0]*(amount+1) for i in range(len(coin)+1)]

    def runStart(self):
        # change 0
        for i in range(len(self.coin)+1):
            self.kmap[i][0] = 1
        for i in range(1,len(self.coin)+1):
            for j in range(1,self.amount+1):
                self.kmap[i][j] = self.kmap[i-1][j] + (self.kmap[i][j-self.coin[i-1]] if self.coin[i-1]<=j  else 0)



coinExchanger = coinExchanger(1000,[10,50,100,500])
coinExchanger.runStart()
print(coinExchanger.kmap)


# def change(amount: int, coins) -> int:
#         # DP[i][j]表示使用前i種銅版，湊j元有幾組解
#         DP = [[0]*(amount+1) for i in range(len(coins)+1)]
        
#         for i in range(len(DP)):
#             DP[i][0] = 1; #湊0元都是一種方法

#         for i in range(1, len(DP)):
#             for j in range(1, len(DP[0])):
#                 DP[i][j] = DP[i-1][j] + (DP[i][j-coins[i-1]] if coins[i-1]<=j else 0)
#         return DP[len(coins)][amount]

# print(change(1000,[10,50,100,500]))