    
n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
m=""
for i in s:
    l.append(i)
    k=m+str(max(l))+" "
print(m.strip())
