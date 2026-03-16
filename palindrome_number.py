n=int(input())
tem=n
rev=0
while n>0:
  rev=(rev*10)+(n%10)
  n=n//10
if n==rev:
  print("palindrome")
else:
  print("Not palindrome")
