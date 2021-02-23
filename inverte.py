lista = []
n=1
while n != 0:
  n= int(input("Digite um número: "))
  if n != 0:
    lista.append(n)
  else: 
    lista.reverse()
    for i in lista:
      print (i)
