n = int(input())
waveAp = []
waveMount = []
while(n!=0):
    input()
    ap = int(input())
    waveAp.append(ap)
    mount = int(input())
    waveMount.append(mount)
    n-=1

for i in range(len(waveAp)):
    for j in range(waveMount[i]):
        for t in range(1,waveAp[i]+1):
            for x in range(1,t+1):
                print(t,end="")
            print()    
        t=waveAp[i]-1
        while(t!=0):
            for x in range(1,t+1):
                print(t,end="")
            print()    
            t-=1
        print()        