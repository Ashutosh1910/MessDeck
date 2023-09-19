str1=input("enter the first string:")
str2=input("enter the second string:")
a1=[]
a2=[]
t=0
for i in str1:
    a1.append(i)



for j in str2:
    a2.append(j)

for k in a1:

    if k  in a2:
        t=t+1

b=len(a2)


if t==(b) and len(a1)==b:
    print("equal")
else:
    print("not")
