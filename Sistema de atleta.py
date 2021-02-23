def main():
    while True:
        opcao = menu()
        executar(opcao)


def menu():
    return input(
        "Bem vindo ao Sistema de Cadastro de Atletas!                                            Escolha o esporte que deseja pesquisar:                                                             1.Futebol                                                                                             2.Vôlei                                                                                                3.Judô                                                                                                 4.Atletismo                                                                                               0.Sair                                                                                                       "
    )


def executar(opcao):
    if (opcao == "1"):
        v_chute = input("Velocidade do chute:")
        print(ler_entrada())
        print("Velocidade do chute:", v_chute)

    elif (opcao == "2"):
        v_saque = input("Velocidade do saque:")
        print(ler_entrada())
        print("Velocidade do saque:", v_saque)

    elif (opcao == "3"):
        p_golpe = input("Principal golpe:")
        print(ler_entrada())
        print("Principal golpe:", v_chute)

    elif (opcao == "4"):
        prova_t = input("Melhor prova e tempo:")
        print(ler_entrada())
        print("melhor prova e tempo:", prova_t)

    else:
        sys.exit(0)


def ler_entrada():
    nome = input("Nome do atleta:")
    idade = int(input("Idade do atleta:"))
    peso = int(input("Peso do atleta:"))
    altura = int(input("Altura do atleta:"))
    return dados(nome, idade, peso, altura)


def dados(nome, idade, peso, altura):
    print("Nome:", nome, "Idade:", idade, "Peso:", peso, "Altura:", altura)


if __name__ == '__main__':
    main()
