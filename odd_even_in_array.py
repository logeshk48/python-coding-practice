n=int(input())
b=list(map(int,input().split()))
o=[]
e=[]
od=0
ev=0
for i in b:
  if i%2!=0:
    odd=odd+1
    o.append(i)

  else:
    even=even+1
    e.append(i)

print(o)
print("odd:",od)
print(e)
print("even:",ev)
