a=int(input())
b=int(input())
for n in range(a,b+1):
    temp=n
    rev=0
    while temp>0:
      rev=(rev*10)+(temp%10)
      temp=temp//10
    if rev==n:
      print(n)
