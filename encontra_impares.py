def encontra_impares(lista):
  if len(lista) ==0:
    return lista
  else:
    impares = []
    if lista[0] % 2 != 0:
      impares.append(lista[0])
    impares.extend(encontra_impares(lista[1:]))

    return impares