n=int(input("enter n"))
t=1
m=n
b=1
a1=[[0] * n for _ in range(n)]
i=0

for i in range(int((n+1)/2)):
    for j in range(i,n):
        a1[i][j]=t
        t=t+1
    for j in range(i+1,n):
        a1[j][n-1]=t
        t=t+1
    for j in range(n-2,i-1,-1):
        a1[n-1][j]=t
        t=t+1
    for j in range(n-2,i,-1):
        a1[j][i]=t
        t=t+1


    n=n-1

for k in range(m):
    print(a1[k])





