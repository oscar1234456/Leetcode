N_M = []
N = [0,0,0,0,0,0,0,0,0,0]
while True:
    n=int(input())
    if(n==0):
        break
    N_M.append(n)
print(N_M)
for i in range(len(N_M)):
    print("in")
    for j in range(1,10):
        N_num = N_M[i] + j
        s = N_num //10
        if(s==j):
            print("%d "%N_num,end="")