a=int(input())
li=[]
nli=[]
for i in range(a):
    c=int(input())
    li.append(c)
for i in range(a):
    pr=1
    for j in range(a):
        if(i!=j):
            pr=pr*li[j]
    nli.append(pr)
print(nli)
