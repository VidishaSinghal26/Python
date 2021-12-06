a=int(input())
b=int(input())
l1=[]
l2=[]
if b<a or b==a:
   l1=list(map(int,input().strip().split()))[:b]
c=int(input())
if c<a or c==a:
    l2=list(map(int,input().strip().split()))[:c]
if b==c:
    print("unity is strength")
else:
    print("impossible")
        
