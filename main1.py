import math
n=int(input("enter a number"))
root=math.sqrt(n)
if int(root+0.5)**2==n:
  print(n,"is perfect square")
else:
  print(n,"is not perfect square")