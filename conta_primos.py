def primos(n):
  if (
    ((n%2 == 0) or (n%3 == 0) or (n%5 == 0))
    and not
    ((n == 3) or (n == 2) or (n == 5))
    ):
    return False
  else:
    return True

def n_primos(n):  
  soma = 0
  while 1 < n:
    if primos(n):
      soma = soma + 1
    n = n - 1
  return soma