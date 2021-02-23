larg = int(input("digite a largura: "))
h = int(input("digite a altura: "))

linha = 1
coluna = 1
while coluna <= h:
  while linha <= larg:
    print ("#", end = "")
    linha = linha + 1
  coluna = coluna + 1
  print ()
  linha = 1