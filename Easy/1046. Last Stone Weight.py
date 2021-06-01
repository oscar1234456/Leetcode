class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) > 1:
            i = stones.index(max(stones)) #Max value index
            temp = stones.copy()
            temp[i] = -1
            j = temp.index(max(temp)) # Second Max value index
            print("j1,", j)
            print("temp,",temp)

            if stones[i] == stones[j]:
                print("i:",i)
                print("j:", j)
                stones[i] = -100
                stones[j] = -100
                print("stones",stones)
                stones.remove(-100)
                stones.remove(-100)
            else:
                # print(stones[i])
                stones[i] = stones[i]-stones[j]

                del stones[j]
                # print(stones)
        if len(stones)==0:
            return 0
        else:
            return stones[0]

if __name__=="__main__":
    stones = [2,7,4,1,8,1]
    dd = Solution()
    print(dd.lastStoneWeight(stones))


# Runtime: 28 ms, faster than 89.66% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.7 MB, less than 92.70% of Python3 online submissions for Last Stone Weight.
