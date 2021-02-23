n=int(input("Digite um número inteiro:"))

adj="não"
digito1 = n % 10 
while n > 0:
  n //= 10 
  digito2 = n % 10 
  if (digito1 == digito2): 
    adj = "sim" 
  digito1 = digito2 
print(adj)