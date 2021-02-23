def retangulo_vazio(larg, h, caractere):
    print(caractere * larg) 

    for i in range(h-2):
        vazio = (larg - 2) * ' '
        print("%s%s%s" % (caractere, vazio, caractere)) 
    print(caractere * larg) 

larg = int(input("digite a largura: "))
h = int(input("digite a altura: "))
caractere = "#"

retangulo_vazio(larg, h, caractere)