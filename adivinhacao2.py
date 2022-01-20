def jogar():
    import random
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")
    pontos = 1000
    total_tentativas = 0
    NUMERO_SECRETO = random.randrange(1, 101)
    print("Qual nível de dificuldade")
    print("[1] fácil, [2] médio, [3], difícil")
    nivel = int(input("Digite o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 3

    for tentativa in range(1, total_tentativas + 1):

        print("tentativa {} de {}".format(tentativa, total_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Digite um número entre 1 e 100")
            continue

        errou_maior = chute > NUMERO_SECRETO
        errou_menor = chute < NUMERO_SECRETO
        acertou = chute == NUMERO_SECRETO

        if acertou:
            print("Você Acertou")
            print("Você fez {} de 100".format(pontos))
            break

        else:
            if errou_maior:
                print("Você Errou, O seu chute foi maior que o numero secreto")
            elif errou_menor:
                print("Você Errou, O seu chute foi menor que o numero secreto")
                pontos_perdidos = abs(NUMERO_SECRETO - chute)
                pontos = pontos - pontos_perdidos
if(__name__== "__main__"):
    jogar()