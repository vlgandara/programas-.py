def conta_letras(frase, tipo= 'vogais'):

  frase = frase.lower()
  vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
  letras = 0

  for letra in frase:
    if letra.isalpha():
      letras += 1

  consoantes = letras - vogais

  if tipo == 'vogais':
    return vogais
  elif tipo == 'consoantes':
    return consoantes
  else:
    return 0