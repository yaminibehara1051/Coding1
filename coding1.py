a=int(input())
li=[]
for i in range(a):
    c=int(input())
    li=li+[c]
k=int(input())
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if(li[i]+li[j]==k):
            print(li[i],li[j])
