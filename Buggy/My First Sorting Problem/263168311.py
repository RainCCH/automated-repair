t = int(input())

for i in range(t):
  x = int(input())
  y = int(input())
  c = -1 
  if x > y:
    c = x
    x = y
    y = c
  print(str(x) + " " + str(y))