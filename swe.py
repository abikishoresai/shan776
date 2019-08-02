n,m=map(int,input().split())
s=max(n,m)
for i in range(1,s):
	if n%i==0 and m%i==0:
		a=i
if n==1 and m==1:
    a=1
print(a)
