testCaseNum = eval(input())

for i in range(1, testCaseNum+1):
    #i: Case No.
    inputRow = input().split()
    totalCost = int(inputRow[1])
    res = 0
    
    inputRow2 = list(map(int, input().split()))
    
    inputRow2.sort()
    
    for element in inputRow2:
        if element <= totalCost:
            res += 1
            totalCost -= element
            if totalCost==0:
                break
    print("Case #"+str(i)+": "+ str(res))
