n=int(input("how many test cases"))
for k in range(0,n):
    t=[]
    t1=[]
    t2=[]
    a=int(input("no. of elements in the array"))
    print("enter the elements of the array")
    for i in range(a):
        y=int(input())
        t.append(abs(y))
        if i%2==0:
          t1.append(abs(y))
        else:
            t2.append(abs(y))

    x=min(t1)
    f=max(t2)
    g=t.index(x)
    h=t.index(f)
    t[g],t[h]=t[h],t[g]
    s=0
    print(t)
    for j in range(a):
        if j%2==0:
         s=s+t[j]
        else:
          s=s-t[j]

    print(str(s))



