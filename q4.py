import math
print("enter 5 no.s:")
a1=[]
hcf=0
for i in range(5):
    a1.append(int(input(f"enter the {i+1} no.:")))
k=0
t=min(a1)

for j in range(t):
    for a in range(5):
        if a1[a]%(j+1)==0:
         k=k+1


    if k==5:
        hcf=j+1
    k=0


print(str(hcf))
