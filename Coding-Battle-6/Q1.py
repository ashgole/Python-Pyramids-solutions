n=7
for x in range(1,n+1):
 px=1
 for y in range(1,x+1):
  print(px,end=" ")
  px=px * (x-y)//y
 print()