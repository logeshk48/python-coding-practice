n=int(input())
temp=n
rem=0
while temp>0:
  d=temp%10
  rem=rem+d**3
  temp=temp//10
if n==rem:
  print("Armstrong")
else:
  print("Not armstrong")
