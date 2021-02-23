def remove_repetidos(lista):
  lista2 = [] 
  for i in lista:
    if i not in lista2:
      lista2.append(i)
  lista2.sort()
  return lista2

lista = [1, 1, 1, 1, 3, 10, 5, 12, 7, 2, 5, 9, 8, 22, 6]

lista = remove_repetidos(lista)
print (lista)