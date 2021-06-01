testCaseNum = eval(input())
now = 0
while testCaseNum>0:
    matrix = list()
    N = temp = eval(input())
    trace = 0
    rowDup = 0
    colDup = 0
    while temp>0:
        matrix.append(list(map(int, input().split())))
        temp -= 1
        
    for i in range(N):
        trace += matrix[i][i]
    for row in matrix:
        testSet = set()
        for element in row:
            if element in testSet:
                rowDup += 1
                break
            else:
                testSet.add(element)
    for i in range(N):
        testSet = set()
        for j in range(N):
            if matrix[j][i] in testSet:
                colDup+=1
                break
            else:
                testSet.add(matrix[j][i])
    now+=1
    print("Case #"+str(now)+": "+str(trace)+" "+str(rowDup)+" "+str(colDup))
    
    testCaseNum -= 1