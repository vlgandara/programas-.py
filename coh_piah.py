import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
  soma = 0
  for i in range(0,6):
    soma = soma + (abs(as_a[i] - as_b[i]))
  return soma / 6

def calcula_assinatura(texto):
  sentencas = separa_sentencas(texto)
  frases = []
  palavras = []
  tam_m_palavras = 0
  tam_m_sentencas = 0
  compl_sentenca = 0
  t_tk = 0
  RHL = 0
  soma_crt_sentenca = 0
  soma_palavras = 0
  soma_crt_frase = 0
  tam_m_frase = 0
  for sentenca in sentencas:      
    soma_crt_sentenca = soma_crt_sentenca + len(sentenca)        
    l_frases = separa_frases(sentenca)
    for f in l_frases:
      frases.append(f)
  for frase in frases:
    soma_crt_frase = soma_crt_frase + len(frase)
    l_palalavras = separa_palavras(frase)
    for palavra in l_palavras:
      palavras.append(palavra)    
  for palavra in palavras:
      soma_palavras = soma_palavras + len(palavra)
  tam_m_palavras = soma_palavras/len(palavras)
  t_tk = n_palavras_diferentes(palavras)/len(palavras)
  RHL = n_palavras_unicas(palavras)/len(palavras)
  tam_m_sentencas = soma_crt_sentenca / len(sentencas)
  compl_sentenca = len(frases) / len(sentencas)
  tam_m_frase = soma_cart_frase / len(frases)
  return [tam_m_palavras, t_tk, RHL, tam_m_sentencas, compl_sentenca, tam_m_frase]


def avalia_textos(textos, ass_cp):
  COHPIAH = []
  for texto in textos:
    ass_texto = calcula_assinatura(texto)
    COHPIAH.append(compara_assinatura(ass_texto, ass_cp))
  lista = COHPIAH[0]
  copia = 1
  for i in range(1, len(inf)):
    if (lista < COHPIAH[i]):
      copia = i
  return copia



def main():        
  ass = le_assinatura()
  textos = le_textos()
  copia = avalia_textos(textos, ass)
  print("O autor do texto {} está infectado com COH-PIAH".format(copia))

main()
