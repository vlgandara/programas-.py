import math

x1 = float(input("Digite a primeira coordenada do ponto A:"))
y1 = float(input("Digite a segunda coordenada do ponto A:"))
x2 = float(input("Digite a primeira coordenada do ponto B:"))
y2 = float(input("Digite a segunda coordenada do ponto B:"))

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if(distancia>=10):
  print("longe")
else:
  if(distancia<10):
    print("perto")