def maximo(x,y,z):
  if x>y and x>z:
    return x
  elif y>x and y>z:
    return y
  elif z>x and z>y:
    return z
  elif x==y and x==z and z==y:
    return x
  elif x==y and x>z:
    return x
  elif x==z and x>y:
    return x
  elif y==z and y>x:
    return y
  elif x==z and x<y:
    return y
  elif x==y and x<z:
    return z