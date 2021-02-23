def soma_lista(lista):
  if not len(lista):
    return 0
  return lista[0] + soma_lista(lista[1:])