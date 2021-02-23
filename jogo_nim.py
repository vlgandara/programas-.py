def main():
  opcao= input("Bem-vindo ao jogo do NIM! Escolha:1 - para jogar uma partida isolada 2 - para jogar um campeonato")
  if (opcao == "1"):
    return partida()
  elif (opcao == "2"):
    return campeonato()
  else:
    print("Opção inválida!")

def partida():
  n = int(input("Quantas peças? "))
  m = int(input("Limite de peças jogadas? "))
  if (n%(m + 1)!=0):
    print("Computador começa!")
    return computador_escolhe_jogada(n,m)
  else:
    print("Você começa!")
    return usuario_escolhe_jogada(n,m)
 
def computador_escolhe_jogada(n,m):
  if (m !=m):
    print("Oops! Jogada inválida! Tente de novo.")
    return computador_escolhe_jogada(n.m)
  elif (m==1):
    print("O computador tirou uma peça.")
    if ((n-1)>=2):
      print("Agora restam", n-1, "peças no tabuleiro.")
      return usuario_escolhe_jogada(n-1,m)
    elif (n-1==1):
      print("Agora resta apenas uma peça no tabuleiro.")
      return usuario_escolhe_jogada(1,1)
    elif (n-1==0):
      print("Fim do jogo. O computador ganhou!")
  elif (m >=2):
    print("O computador tirou", m, "peças.")
    if ((n-m)>=2):
      print("Agora restam", n-m, "peças no tabuleiro.")
      if((n-m)>=m+1):
        return usuario_escolhe_jogada(n-m,m)
      elif((n-m)<m+1):
        return usuario_escolhe_jogada(n-m,n-m)
    elif (n-m==1):
      print("Agora resta apenas uma peça no tabuleiro.")
      return usuario_escolhe_jogada(1,1)
    elif (n-m==0):
      print("Fim do jogo. O computador ganhou!")
                         
def usuario_escolhe_jogada(n,m):
  peças_tiradas= int(input("Quantas peças você vai tirar? "))
  if (peças_tiradas !=m):
    print("Oops! Jogada inválida! Tente de novo.")
    return usuario_escolhe_jogada(n,m)  
  elif (peças_tiradas == 1):
    print("Voce tirou uma peça.")
    if ((n-1)>2):
      print("Agora restam", n-1, "peças no tabuleiro.")
      return computador_escolhe_jogada(n-1,m)
    elif (n-peças_tiradas==1):
      print("Agora resta apenas uma peça no tabuleiro.")
      return computador_escolhe_jogada(n-1,1)
    elif ((n-peças_tiradas)==0):
      print("Fim do jogo. Você ganhou!")
  elif (peças_tiradas >=2):
    print("Você tirou", peças_tiradas, "peças.")
    if ((n-peças_tiradas)>=2):
      print("Agora restam", n-peças_tiradas, "peças no tabuleiro.")
      if((n-peças_tiradas)>=peças_tiradas+1):
        return computador_escolhe_jogada(n-peças_tiradas,m)
      elif((n-peças_tiradas)<peças_tiradas+1):
        return computador_escolhe_jogada(n-peças_tiradas,n-peças_tiradas)
    elif (n-peças_tiradas==1):
      print("Agora resta apenas uma peça no tabuleiro.")
      return computador_escolhe_jogada(1,1)
    elif (n-peças_tiradas==0):
      print("Fim do jogo. Você ganhou!")

def campeonato():
  numeroRodada = 1
  while numeroRodada <= 3:
    print()
    print('**** Rodada', numeroRodada, '****')
    print()
    partida()
    numeroRodada += 1
  print()
  print("Placar: Você 0 X 3 Computador")

if __name__=="__main__":
  main()
