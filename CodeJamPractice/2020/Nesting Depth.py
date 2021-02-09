testCaseNum = eval(input())

for i in range(1,testCaseNum+1):
    # i :case No.
    open = 0
    res = ""
    nums = input()
    for element in nums:
        now = int(element)
        while open < now:
            res += "("
            open += 1
        while open > now:
            res += ")"
            open -= 1
        
        res += element

    while open > 0:
        res += ")"
        open -= 1
        
    print("Case #"+str(i)+": "+res)