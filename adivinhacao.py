import random

def jogar():

    dificuldade = input("Facil, Médio ou Difícil? ")
    if (dificuldade == "facil"):
        tentativa = 5
        numeroSegredo = random.randrange(1, 11)
    elif (dificuldade == "medio"):
        tentativa = 10
        numeroSegredo = random.randrange(1, 51)
    else:
        tentativa = 25
        numeroSegredo = random.randrange(1, 101)

    pontos = 1000
    totalTentativas = tentativa

    for tentativa in range(1, totalTentativas + 1):
        print(numeroSegredo)
        print("tentativa: {} de {}!" .format(tentativa, totalTentativas))
        chute_str = input("Digite aqui um numero entre 1 e 100: ");
        chute = int(chute_str);
    

        if(chute < 1 or chute > 100):
            print("O número deve ser entre 1 e 100!");
            continue

        acertou = numeroSegredo == chute
        maior = numeroSegredo > chute


        if(acertou):
            print("voce acerto");
            break;

        else:
            if(maior):
                print("voce errou, joga um maior");
            else:
                print("voce erro, joga um menor");

            pontosPerdidos = abs(numeroSegredo - chute)
            pontos = pontos - pontosPerdidos
    print("Fim e jogo! Sua pontuação total foi: {}" .format(pontos))
    
if (__name__ == "__main__"):
    jogar()