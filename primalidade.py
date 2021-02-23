inteiro=int(input("Digite um número inteiro:"))

i=2
primo=True

while (i<inteiro and primo):
  primo=not(inteiro%i==0)
  i+=1

if(primo):
  print("primo")
else:
  print("não primo")