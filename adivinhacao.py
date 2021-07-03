import random
def jogar():

    continuar = 1
    while (continuar == 1):
        print("*********************************")
        print("Bem vindo ao jogo de Adivinhação!")
        print("*********************************")

        numero_secreto = random.randrange(1, 101)
        total_de_tentativas = 0
        pontos = 1000

        print("Nível de difículdade")
        print("(1) Fácil (2) Médio (3) Difícil")

        nivel = int(input("Nível de díficuldade"))

        if (nivel == 1):
            total_de_tentativas = 20
        elif(nivel == 2):
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5
        for rodada in range (1, total_de_tentativas +1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute = int(input("digite um número"))
            print("Você digitou", chute)

            if(chute < 1 or chute > 100):
                print("Você deve digitar um númeroentre 1 e 100")
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if (acertou):
                print("Você acertou!")
                break
            else:
                if (maior):
                    print("Você errou! O seu chute foi maior que o número secreto.")
                elif (menor):
                    print("Você errou! O seu chute foi menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
            rodada = rodada + 1
        print("Você conquistou", pontos, "pontos")

        print("Fim do jogo\n")

        print("Deseja continuar?")
        print("Sim(1) ou Não(0)")
        continuar = int(input("Decidiu?"))

    print("Obrigado por participar.")
if (__name__ == "__main__"):
    jogar()