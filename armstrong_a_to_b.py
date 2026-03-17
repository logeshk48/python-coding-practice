a=int(input())
b=int(input())
for n in range(a,b+1):
  temp=n
  rem=0
  while temp>0:
    digit=digit%10
    rem=rem+digit**3
    digit=digit//10
  if(n==rem):
    print(n)
