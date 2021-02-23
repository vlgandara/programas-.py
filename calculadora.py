import math

def main():
  opcao = input(''' Bem-vindo a minha calculadora em Python!

  Digite uma das opçõões abaixo:

  1 - Adição
  2 - Subtração
  3 - Multiplicação
  4 - Divisão
  5 - Potenciação
  6 - Raiz Quadrada
  7 - Logarítimo_base_dez
  8 - Seno 
  9 - Cosseno
  10 - Tangente
  11 - Conversor AngXRadianos
  ''')
  

  if (opcao =="1"):
    entrada1 = float(input("Digite o primeiro número:"))
    entrada2 = float(input("Digite o segundo número:"))
    print(Adição(entrada1,entrada2))
  elif (opcao =="2"):
    entrada1 = float(input("Digite o primeiro número:"))
    entrada2 = float(input("Digite o segundo número:"))
    print(Subtração(entrada1,entrada2))
  elif (opcao =="3"):
    entrada1 = float(input("Digite o primeiro número:"))
    entrada2 = float(input("Digite o segundo número:"))
    print(Multiplicação(entrada1,entrada2))
    entrada1 = float(input("Digite o primeiro número:"))
    entrada2 = float(input("Digite o segundo número:"))
  elif (opcao =="4"):
    entrada1 = float(input("Digite o primeiro número:"))
    entrada2 = float(input("Digite o segundo número:"))
    print(Divisão(entrada1,entrada2))
  elif (opcao =="5"):
    entrada1 = float(input("Digite o primeiro número:"))
    entrada2 = float(input("Digite o segundo número:"))
    print(pow(entrada1,entrada2))
  elif (opcao =="6"):
    entrada1 = float(input("Digite o primeiro número:"))
    print(math.sqrt(entrada1))
  elif (opcao =="7"):
    entrada1 = float(input("Digite o primeiro número:"))
    print(math.log10(entrada1))
  elif (opcao =="8"):
    entrada1 = float(input("Digite o primeiro número:"))
    print(math.sin(entrada1))
  elif (opcao =="9"):
    entrada1 = float(input("Digite o primeiro número:"))
    print(math.cos(entrada1))
  elif (opcao =="10"):
    entrada1 = float(input("Digite o primeiro número:"))
    print(math.tan(entrada1))
  elif (opcao =="11"):
    entrada1 = float(input("Digite o primeiro número:"))
    print(math.radians(entrada1))

  else:
    print("Operação Invãlida!")
  
def Adição(entrada1,entrada2):
    return(entrada1 + entrada2)

def Subtração(entrada1,entrada2):
  return(entrada1 - entrada2)

def Multiplicação(entrada1,entrada2):
  return(entrada1 * entrada2)

def Divisão(entrada1,entrada2):
  return(entrada1 / entrada2)

if __name__ == '__main__':
  main()
    