def valor(n):
  a=0
  b=1
  i=1
  c=a+b
  print(a, b, 1)
  while (i<n):
    i=i+1
    a=b
    b=c
    c=a+b
    print(c)